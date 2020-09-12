package com.johnson.ender.siziba.financialinstitutionsmgt;

import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import com.johnson.ender.siziba.financialinstitutionsmgt.database.DBManager;

import java.io.IOException;
import java.io.InputStream;

public class Read extends AppCompatActivity {
    String pageLink = "";
    String pageTitle = "";
    String pageIntro = "";
    boolean pageIsBookmarked = false;

    private DBManager dbManager;

    private Menu mainMenu;

    String initLink;

    WebView htmlWebView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setupToolbar();
        initLink = getIntent().getStringExtra("THE_LINK");
        setContentView(R.layout.activity_read);

        htmlWebView = findViewById(R.id.theWebview);
        WebSettings webSetting = htmlWebView.getSettings();
        webSetting.setJavaScriptEnabled(true);
        webSetting.setAllowUniversalAccessFromFileURLs(true);
        webSetting.setDisplayZoomControls(false);
        htmlWebView.addJavascriptInterface(this, "JSReceiver");

        final AlertDialog alertDialog = new AlertDialog.Builder(this).create();
        //    private GalleryViewModel galleryViewModel;
        final ProgressDialog progressBar = ProgressDialog.show(Read.this, "Please Wait", "Loading...");


        htmlWebView.setWebChromeClient(new WebChromeClient() {
            public void onProgressChanged(WebView view, int progress) {

            }
        });
        htmlWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                Log.i("Email", "Processing webview url click...");
                view.loadUrl(url);
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);

                // Inject CSS when page is done loading
                //injectCSS(view);

                //injectScriptFile(view, "js/javascript.js"); // see below ...

                // test if the script was loaded
                //view.loadUrl("javascript:setTimeout(test(), 500)");

                Log.i("Read", "Finished loading URL: " + url);
                if (progressBar.isShowing()) {
                    progressBar.dismiss();
                }
            }

            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                Log.e("Email", "Error: " + description);
                Toast.makeText(Read.this, "Oh no! " + description, Toast.LENGTH_SHORT).show();
                alertDialog.setTitle("Error");
                alertDialog.setMessage(description);
                alertDialog.setButton("OK", new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        return;
                    }
                });
                alertDialog.show();
            }

            private void injectScriptFile(WebView view, String scriptFile) {
                InputStream input;
                try {
                    input = getAssets().open(scriptFile);
                    byte[] buffer = new byte[input.available()];
                    input.read(buffer);
                    input.close();

                    // String-ify the script byte-array using BASE64 encoding !!!
                    String encoded = Base64.encodeToString(buffer, Base64.NO_WRAP);
                    view.loadUrl("javascript:(function() {" +
                            "var parent = document.getElementsByTagName('head').item(0);" +
                            "var script = document.createElement('script');" +
                            "script.type = 'text/javascript';" +
                            // Tell the browser to BASE64-decode the string into your script !!!
                            "script.innerHTML = window.atob('" + encoded + "');" +
                            "parent.appendChild(script)" +
                            "})()");
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }////

            private void injectCSS(WebView view) {
                try {
                    InputStream inputStream = getAssets().open("style.css");
                    byte[] buffer = new byte[inputStream.available()];
                    inputStream.read(buffer);
                    inputStream.close();
                    String encoded = Base64.encodeToString(buffer, Base64.NO_WRAP);
                    view.loadUrl("javascript:(function() {" +
                            "var parent = document.getElementsByTagName('head').item(0);" +
                            "var style = document.createElement('style');" +
                            "style.type = 'text/css';" +
                            // Tell the browser to BASE64-decode the string into your script !!!
                            "style.innerHTML = window.atob('" + encoded + "');" +
                            "parent.appendChild(style)" +
                            "})()");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });


        htmlWebView.loadUrl(initLink);//automata_theory/index.htm
        //htmlWebView.loadUrl("file:///android_asset/automata_theory/index.htm");//automata_theory/index.htm

    }

    public void setupToolbar() {
        //Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        // setSupportActionBar(toolbar);
        final ActionBar ab = getSupportActionBar();
        if(ab != null) {
            ab.setDisplayHomeAsUpEnabled(true);
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            // Respond to the action bar's Up/Home button
            case android.R.id.home:
                startActivity(new Intent(this, MainActivity.class));
                finish();
                return true;
            case  R.id.Menu_Bookmark:
                if (pageIsBookmarked) {
                    removeBookmark();
                }
                else {
                    addBookmark();
                }
                break;

            case R.id.Menu_Contents:
                htmlWebView.loadUrl("javascript:contents()");
                break;

        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.options_menu,menu);
        this.mainMenu = menu;
        return super.onCreateOptionsMenu(menu);
    }

    @JavascriptInterface
    public void test(){
        ;
    }

    @JavascriptInterface
    public void getPageDetails(String title, String link, String intro){
        Log.i("Read", "Title: " + title);
        Log.i("Read", "Link: " + link);
        //return new String[]{title, link};
        this.pageLink = link;
        this.pageTitle = title;
        this.pageIntro = intro;

        pageOpenTasks();
    }

    public void setTitle(){
        try {
            getSupportActionBar().setTitle(pageTitle);
        }
        catch (Exception ignored){
            ;
        }
    }

    public void savePageDetails(){
        dbManager = new DBManager(this);
        dbManager.open();
        dbManager.insert(pageTitle, pageLink, pageIntro, "history");
        dbManager.close();
    }

    public void pageOpenTasks(){
        setTitle();
        savePageDetails();
        setPageBookmarkedIcon();
    }

    public boolean isPageBookmarked(){
        dbManager = new DBManager(this);
        dbManager.open();
        boolean out = dbManager.isPageBookmarked(pageLink);
        dbManager.close();
        return out;
    }

    public void setPageBookmarkedIcon(){
        this.pageIsBookmarked = isPageBookmarked();
        if (pageIsBookmarked){
            if (mainMenu != null) {
                MenuItem item = mainMenu.findItem(R.id.Menu_Bookmark);
                if (item != null) {
                    item.setIcon(R.drawable.ic_star);
                }
            }
        }

        else {
            if (mainMenu != null) {
                MenuItem item = mainMenu.findItem(R.id.Menu_Bookmark);
                if (item != null) {
                    item.setIcon(R.drawable.ic_star_border_black);
                }
            }
        }
    }

    public void addBookmark(){
        dbManager = new DBManager(this);
        dbManager.open();
        dbManager.insert(pageTitle, pageLink, pageIntro, "bookmark");
        dbManager.close();
        setPageBookmarkedIcon();
    }

    public void removeBookmark(){
        dbManager = new DBManager(this);
        dbManager.open();
        dbManager.deleteBookmark(pageLink);
        dbManager.close();
        setPageBookmarkedIcon();
    }


    @Override
    public void onBackPressed() {
        if (htmlWebView.canGoBack()) {
            htmlWebView.goBack();
        } else {
            startActivity(new Intent(this, MainActivity.class));
            finish();
        }
    }
}
