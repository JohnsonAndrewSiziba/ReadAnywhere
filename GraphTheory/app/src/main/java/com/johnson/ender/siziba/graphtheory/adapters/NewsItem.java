package com.johnson.ender.siziba.graphtheory.adapters;

public class NewsItem {


    String Title,Content,Date, Link;
    int userPhoto;

    public NewsItem() {
    }


    public NewsItem(String title, String content, String date, int userPhoto, String link) {
        Title = title;
        Content = content;
        Date = date;
        Link = link;
        this.userPhoto = userPhoto;
    }

    public void setTitle(String title) {
        Title = title;
    }

    public void setContent(String content) {
        Content = content;
    }

    public void setDate(String date) {
        Date = date;
    }

    public void setUserPhoto(int userPhoto) {
        this.userPhoto = userPhoto;
    }

    public String getTitle() {
        return Title;
    }

    public String getContent() {
        return Content;
    }

    public String getDate() {
        return Date;
    }

    public int getUserPhoto() {
        return userPhoto;
    }

    public String getLink() {
        return Link;
    }

    public void setLink(String link) {
        Link = link;
    }
}
