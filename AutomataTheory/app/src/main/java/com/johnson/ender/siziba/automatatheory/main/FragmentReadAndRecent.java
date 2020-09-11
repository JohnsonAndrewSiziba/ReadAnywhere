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

    private List<NewsItem> mData;


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

        ConstraintLayout rootLayout = getActivity().findViewById(R.id.frame_layout);
        RecyclerView newsRecyclerview = getActivity().findViewById(R.id.my_rv);
        mData = new ArrayList<>();

        addData();

        boolean isDark = false;
        NewsAdapter newsAdapter = new NewsAdapter(getActivity(), mData, isDark);
        newsRecyclerview.setAdapter(newsAdapter);
        newsRecyclerview.setLayoutManager(new LinearLayoutManager(getActivity()));

        scanButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                startActivity(new Intent(getActivity(), Read.class));
                Intent intent = new Intent(getActivity(), Read.class);
                intent.putExtra("THE_LINK", "file:///android_asset/automata_theory/index.htm");
                startActivity(intent);
                getActivity().finish();
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
                String intro = cursor.getString(cursor.getColumnIndex("intro"));
                String path = cursor.getString(cursor.getColumnIndex("path"));
                String type = cursor.getString(cursor.getColumnIndex("type"));
                long time = cursor.getLong(cursor.getColumnIndex("time_created"));
                String theTime = TimeUtility.timeAgo(time);

                NewsItem newsItem = new NewsItem(title, intro, theTime, R.drawable.ic_info_black, path);

                mData.add(newsItem);

            }while(cursor.moveToNext());
        }
        cursor.close();

    }
}
