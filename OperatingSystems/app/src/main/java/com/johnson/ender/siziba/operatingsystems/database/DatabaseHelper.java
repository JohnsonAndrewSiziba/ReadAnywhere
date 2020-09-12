package com.johnson.ender.siziba.operatingsystems.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {

    // Database Information
    static final String DB_NAME = "OPERATINGSYSYTEMS.DB";
    static final int DB_VERSION = 2;


    // Table Names
    public static final String TABLE_LINKS_NAME = "LINKS";

    //============================== Table columns ===========================

    public static final String ID = "_id";
    public static final String TIME_CREATED = "time_created";
    public static final String TITLE = "title";
    public static final String PATH = "path";
    public static final String INTRO = "intro";
    public static final String TYPE = "type";



    //============================== Create Table Queries ===========================

    private static final String CREATE_TABLE = "create table "
            + TABLE_LINKS_NAME + "(" +
            ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
            TITLE + " TEXT, " +
            PATH + " TEXT, " +
            INTRO + " TEXT, " +
            TYPE + " TEXT, " +
            TIME_CREATED + " INTEGER);";


    //============================================================

    public DatabaseHelper(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_TABLE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_LINKS_NAME);
        onCreate(db);
    }

}
