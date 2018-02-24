package com.thc.bestpig.serial;

import android.annotation.TargetApi;
import android.content.DialogInterface;
import android.os.Build;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.InputFilter;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    protected boolean validateSerial(String serial) {
        if (serial.charAt(4) != '-' || serial.charAt(9) != '-' || serial.charAt(14) != '-')
            return false;
        if ((int)serial.charAt(5) != (int) serial.charAt(6) + 1)
            return false;

        if (serial.charAt(5) != serial.charAt(18))
            return false;

        if ((int) serial.charAt(1) != (((int)serial.charAt(18)) % 4) * 22)
            return false;
        if ((((int)(serial.charAt(3))*(int)(serial.charAt(15)))/(int)(serial.charAt(17)))-1 != (int)(serial.charAt(10)))
            return false;
        if (serial.charAt(10) != serial.charAt(1))
            return false;
        if ((int)(serial.charAt(13)) != (int)(serial.charAt(10)) + 5)
            return false;
        if ((int)(serial.charAt(10)) != (int)(serial.charAt(5)) - 9)
            return false;
        if (((int)(serial.charAt(0)) % (int)(serial.charAt(7))) * (int)(serial.charAt(11)) != 1440)
            return false;
        if (((int)(serial.charAt(2)) - (int)(serial.charAt(8)) + (int)(serial.charAt(12))) != ((int)(serial.charAt(10)) - 9))
            return false;
        if ((((int)(serial.charAt(3)) + (int)(serial.charAt(12))) / 2) != (int)(serial.charAt(16)))
            return false;
        if (((int)(serial.charAt(0)) - (int)(serial.charAt(2)) + (int)(serial.charAt(3))) != ((int)(serial.charAt(12)) + 15))
            return false;
        if (serial.charAt(3) != serial.charAt(13))
            return false;
        if (serial.charAt(16) != serial.charAt(0))
            return false;
        if ((int)(serial.charAt(7)) + 1 != (int)(serial.charAt(2)))
            return false;
        if ((int)(serial.charAt(15)) + 1 != (int)(serial.charAt(11)))
            return false;
        if ((int)(serial.charAt(11)) + 3 != (int)(serial.charAt(17)))
            return false;
        if ((int)(serial.charAt(7)) + 20 != (int)(serial.charAt(6)))
            return false;

        return true;
    }

    protected void checkPassword(String serial) {
        if (validateSerial(serial)) {
            new AlertDialog.Builder(MainActivity.this)
                    .setTitle("Well done ;)")
                    .setMessage("You can now validate ths challenge.\n\nThe flag is the serial")
                    .setCancelable(false)
                    .setNeutralButton("Ok", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                        }
                    }).show();
        }
        else {
            new AlertDialog.Builder(MainActivity.this)
                    .setTitle("Premium activation failed")
                    .setMessage("Please don't try random serial, buy a legit premium license to support developers.")
                    .setCancelable(false)
                    .setNeutralButton("Ok", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                        }
                    }).show();
        }
    }

    @TargetApi(Build.VERSION_CODES.LOLLIPOP)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setLogo(R.mipmap.ic_launcher);
        getSupportActionBar().setDisplayUseLogoEnabled(true);

        final EditText editText = findViewById(R.id.serialInput);

        editText.setFilters(new InputFilter[] {
                new InputFilter.AllCaps(),
                new InputFilter.LengthFilter(19)
        });

        Button clickButton = findViewById(R.id.buttonActivate);
        clickButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkPassword(editText.getText().toString());
            }
        });
    }
}
