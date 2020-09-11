package com.johnson.ender.siziba.automatatheory.main;

import android.database.Cursor;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.johnson.ender.siziba.automatatheory.R;
import com.johnson.ender.siziba.automatatheory.adapters.BookmarksAdapter;
import com.johnson.ender.siziba.automatatheory.adapters.NewsAdapter;
import com.johnson.ender.siziba.automatatheory.adapters.NewsItem;
import com.johnson.ender.siziba.automatatheory.database.DBManager;
import com.johnson.ender.siziba.automatatheory.helpers.TimeUtility;

import java.util.ArrayList;
import java.util.List;

public class FragmentBookmarks extends Fragment {
    private List<NewsItem> mData;

    public FragmentBookmarks() {
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
        return inflater.inflate(R.layout.fragment_bookmarks, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        ConstraintLayout rootLayout = getActivity().findViewById(R.id.bookmarks_frame);
        RecyclerView bookmarksRv = getActivity().findViewById(R.id.bookmarks_rv);
        mData = new ArrayList<>();

        addData();

        boolean isDark = false;
        NewsAdapter bookmarksAdapter = new NewsAdapter(getActivity(), mData, isDark);
        bookmarksRv.setAdapter(bookmarksAdapter);
        bookmarksRv.setLayoutManager(new LinearLayoutManager(getActivity()));
    }

    public void addData(){
        DBManager dbManager = new DBManager(getActivity());
        dbManager.open();
        Cursor cursor =  dbManager.fetch("bookmark");
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

            }   while(cursor.moveToNext());
        }
        cursor.close();

    }


}
