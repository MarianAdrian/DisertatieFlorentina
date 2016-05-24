package marian.demofacedetection;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import org.opencv.android.OpenCVLoader;
import org.opencv.objdetect.CascadeClassifier;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    static
    {
        if(!OpenCVLoader.initDebug())
        {
            Log.d(TAG, "OpenCV not loaded");
        }
        else
        {
            Log.d(TAG, "OpenCV loaded");
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        CascadeClassifier faceCascade = new CascadeClassifier("haarcascade_frontalface_default.xml");
        setContentView(R.layout.activity_main);
    }
}
