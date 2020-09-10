package com.johnson.ender.siziba.automatatheory.main;

import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;


import com.johnson.ender.siziba.automatatheory.R;
import com.johnson.ender.siziba.automatatheory.Read;
import com.johnson.ender.siziba.automatatheory.adapters.NewsAdapter;
import com.johnson.ender.siziba.automatatheory.adapters.NewsItem;
import com.johnson.ender.siziba.automatatheory.database.DBManager;
import com.johnson.ender.siziba.automatatheory.helpers.TimeUtility;

import java.util.ArrayList;
import java.util.List;


public class FragmentReadAndRecent extends Fragment {

    RecyclerView NewsRecyclerview;
    NewsAdapter newsAdapter;
    List<NewsItem> mData;
    ConstraintLayout rootLayout;
    boolean isDark = false;


    public FragmentReadAndRecent() {
        // Required empty public constructor
    }


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_read_and_recent, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        Button scanButton = (getActivity()).findViewById(R.id.button2);

        rootLayout = getActivity().findViewById(R.id.frameLayout);
        NewsRecyclerview = getActivity().findViewById(R.id.news_rv);
        mData = new ArrayList<>();

        addData();

        newsAdapter = new NewsAdapter(getActivity(),mData,isDark);
        NewsRecyclerview.setAdapter(newsAdapter);
        NewsRecyclerview.setLayoutManager(new LinearLayoutManager(getActivity()));

        scanButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getActivity(), Read.class));
//                getActivity().finish();
            }
        });

    }

    public void addData(){
//        mData.add(new NewsItem("Successful Scan","Lorem ipsum  labore et dolore magna aliqua. Ut enim.","6 July",R.drawable.ic_info_black));
        DBManager dbManager = new DBManager(getActivity());
        dbManager.open();
        Cursor cursor =  dbManager.fetch("history");
        dbManager.close();

        if (cursor.moveToFirst()){
            do{
                int id = cursor.getInt(cursor.getColumnIndex("_id"));
                String title = cursor.getString(cursor.getColumnIndex("title"));
                String path = cursor.getString(cursor.getColumnIndex("path"));
                String type = cursor.getString(cursor.getColumnIndex("type"));
                long time = cursor.getLong(cursor.getColumnIndex("time_created"));
                String theTime = TimeUtility.timeAgo(time);

                NewsItem newsItem = new NewsItem(title.substring(0, Math.min(title.length(), 12)), title, theTime, R.drawable.ic_info_black);

                mData.add(newsItem);

            }while(cursor.moveToNext());
        }
        cursor.close();

    }
}
