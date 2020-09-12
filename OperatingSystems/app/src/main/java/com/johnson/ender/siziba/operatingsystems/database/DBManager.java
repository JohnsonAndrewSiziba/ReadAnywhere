package com.johnson.ender.siziba.operatingsystems.database;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;

import java.sql.Timestamp;


public class DBManager {
    private DatabaseHelper dbHelper;

    private Context context;

    private SQLiteDatabase database;

    public DBManager(Context c) {
        context = c;
    }

    public DBManager open() throws SQLException {
        dbHelper = new DatabaseHelper(context);
        database = dbHelper.getWritableDatabase();
        return this;
    }

    public void close() {
        dbHelper.close();
    }

    public void insert(String title, String path, String intro, String type) {
        Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        long millis = timestamp.getTime();

        ContentValues contentValue = new ContentValues();
        contentValue.put(DatabaseHelper.TITLE, title.substring(0, Math.min(title.length(), 23)));
        contentValue.put(DatabaseHelper.PATH, path);
        contentValue.put(DatabaseHelper.TYPE, type);
        contentValue.put(DatabaseHelper.INTRO, intro.substring(0, Math.min(intro.length(), 100)));
        contentValue.put(DatabaseHelper.TIME_CREATED, millis);
        database.insert(DatabaseHelper.TABLE_LINKS_NAME, null, contentValue);
    }

    public Cursor fetch(String type) {
        String[] columns = new String[] { DatabaseHelper.ID, DatabaseHelper.TITLE, DatabaseHelper.PATH, DatabaseHelper.TIME_CREATED };
//        Cursor cursor = database.query(DatabaseHelper.TABLE_LINKS_NAME, columns, null, DatabaseHelper.TYPE + " = " + type, null, null, null);

        String query = "SELECT * FROM " + DatabaseHelper.TABLE_LINKS_NAME + " WHERE " + DatabaseHelper.TYPE + " = ? ORDER BY " + DatabaseHelper.TIME_CREATED +" DESC LIMIT 100";
        Cursor cursor = database.rawQuery(query, new String[] {type});
        if (cursor != null) {
            cursor.moveToFirst();
        }
        return cursor;
    }
//
//    public int update(long _id, String name, String desc) {
//        ContentValues contentValues = new ContentValues();
//        contentValues.put(DatabaseHelper.SUBJECT, name);
//        contentValues.put(DatabaseHelper.DESC, desc);
//        int i = database.update(DatabaseHelper.TABLE_NAME, contentValues, DatabaseHelper._ID + " = " + _id, null);
//        return i;
//    }
//
    public void deleteHistory(String link) {
        database.delete(DatabaseHelper.TABLE_LINKS_NAME, DatabaseHelper.PATH + "=" + link, null);
    }

    public void deleteBookmark(String link) {
        database.delete(DatabaseHelper.TABLE_LINKS_NAME,
                DatabaseHelper.PATH + "= '" + link + "' AND " + DatabaseHelper.TYPE + "= 'bookmark'",
                null);
    }

    public boolean isPageBookmarked(String path){
        String query = "SELECT * FROM " + DatabaseHelper.TABLE_LINKS_NAME + " WHERE " + DatabaseHelper.PATH + " = '" + path + "' AND " + DatabaseHelper.TYPE + " = 'bookmark'";

        Cursor cursor = database.rawQuery(query, null);
        if(cursor.getCount() <= 0){
            cursor.close();
            return false;
        }

        cursor.close();

        return true;
    }
}
