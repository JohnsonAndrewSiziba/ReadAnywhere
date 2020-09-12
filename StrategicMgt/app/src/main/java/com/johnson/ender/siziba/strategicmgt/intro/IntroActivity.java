package com.johnson.ender.siziba.strategicmgt.intro;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import com.google.android.material.tabs.TabLayout;
import com.johnson.ender.siziba.strategicmgt.MainActivity;
import com.johnson.ender.siziba.strategicmgt.R;
import com.johnson.ender.siziba.strategicmgt.helpers.AppValues;


import java.util.ArrayList;
import java.util.List;

public class IntroActivity extends AppCompatActivity {
    private ViewPager screenPager;
    TabLayout tabIndicator;
    Button btnNext;
    int position = 0;
    Button btnGetstarted;
    Animation btnAnim;

    IntroViewPagerAdapter introViewPagerAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_intro);


        btnNext = findViewById(R.id.btnNext);
        btnGetstarted = findViewById(R.id.btnGetStarted);
        tabIndicator = findViewById(R.id.tabIndicator);
        btnAnim = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.btn_animation);

        String lorem = "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter";

        final List<ScreenItem> mlist = new ArrayList<>();
        mlist.add(new ScreenItem("Read Anywhere", "Take your notes with you everywhere.", R.drawable.everywhere));
        mlist.add(new ScreenItem("Succeed!", "Never miss an opportunity to study.", R.drawable.ic_book_lover));
        mlist.add(new ScreenItem("Johnson", "Brought to you by Johnson A. Siziba", R.drawable.johnson));

        screenPager = findViewById(R.id.screenViewPager);
        introViewPagerAdapter = new IntroViewPagerAdapter(this, mlist);
        screenPager.setAdapter(introViewPagerAdapter);

        tabIndicator.setupWithViewPager(screenPager);


        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                position = screenPager.getCurrentItem();
                if (position < mlist.size()){
                    position++;
                    screenPager.setCurrentItem(position);
                }

                if (position >= mlist.size()){
                    loadLastScreen();
                }
//                Toast.makeText(IntroActivity.this, "Posotion: " + position +", size: " + mlist.size(), Toast.LENGTH_SHORT).show();
            }
        });

        tabIndicator.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                if (tab.getPosition() == mlist.size()){
                    loadLastScreen();
                }
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {

            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {

            }
        });

        btnGetstarted.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AppValues.setInit_sequence("done");
                Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(mainActivity);
                finish();
            }
        });

    }

    private void loadLastScreen() {
        btnNext.setVisibility(View.INVISIBLE);
        btnGetstarted.setVisibility(View.VISIBLE);
        tabIndicator.setVisibility(View.INVISIBLE);
        btnGetstarted.setAnimation(btnAnim);
    }
}
