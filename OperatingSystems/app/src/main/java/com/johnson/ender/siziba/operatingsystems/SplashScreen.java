package com.johnson.ender.siziba.operatingsystems;

import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.Window;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.webkit.WebView;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.johnson.ender.siziba.operatingsystems.helpers.AppValues;
import com.johnson.ender.siziba.operatingsystems.helpers.SharedPrefsManager;
import com.johnson.ender.siziba.operatingsystems.intro.IntroActivity;


public class SplashScreen extends AppCompatActivity {

    private static int splashTimeOut=2500;
    ImageView appLogo;
    TextView copyright;
    String init_sequence;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        SharedPrefsManager.init(getApplicationContext());
        AppValues.init();
        init_sequence = AppValues.getInit_sequence();


        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();

        setContentView(R.layout.activity_splash_screen);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            if (0 != (getApplicationInfo().flags & ApplicationInfo.FLAG_DEBUGGABLE))
            { WebView.setWebContentsDebuggingEnabled(true); }
        }

        appLogo = findViewById(R.id.appLogo);
        copyright = findViewById(R.id.copyright);

        Animation fadeIn = AnimationUtils.loadAnimation(this,R.anim.animation_fade_id);
        Animation translate = AnimationUtils.loadAnimation(this,R.anim.animation_translation);

        appLogo.startAnimation(fadeIn);

        copyright.startAnimation(translate);

        copyright.startAnimation(translate);


        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {

                Intent forwardIntent;
                Log.d("Splash", init_sequence);
                if(init_sequence.equals("done")) {
                    forwardIntent = new Intent(SplashScreen.this, MainActivity.class);
                }
                else {
                    forwardIntent = new Intent(SplashScreen.this, IntroActivity.class);
                }

                startActivity(forwardIntent);
                finish();
            }
        },2000);


    }
}
