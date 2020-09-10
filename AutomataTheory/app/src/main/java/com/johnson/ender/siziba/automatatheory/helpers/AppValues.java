package com.johnson.ender.siziba.automatatheory.helpers;

public class AppValues {
    private static AppValues instance;
    private static String init_sequence;

    private AppValues() {
        init_sequence = SharedPrefsManager.read("init_sequence", "none");
    }

    public static void init()
    {
        if (null == instance)
            instance = new AppValues();
    }

    public static String getInit_sequence() {
        return init_sequence;
    }

    public static void setInit_sequence(String init_s) {
        SharedPrefsManager.write("init_sequence", init_s);
        AppValues.init_sequence = init_s;
    }

}
