package com.johnson.ender.siziba.internationalfinance.main;


import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

public class TabPagerAdapter extends FragmentPagerAdapter {
    int tabCount;
    public TabPagerAdapter(FragmentManager fm, int numberOfTabs) {
        super(fm);
        this.tabCount = numberOfTabs;
    }
    @Override
    public Fragment getItem(int position) {
        switch (position) {
            case 0:
                FragmentReadAndRecent tab1 = new FragmentReadAndRecent();
                return tab1;
            case 1:
                FragmentBookmarks tab2 = new FragmentBookmarks();
                return tab2;
            default:
                return null;
        }
    }
    @Override
    public int getCount() {
        return tabCount;
    }
}
