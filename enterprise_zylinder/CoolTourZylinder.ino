
// Adafruit_NeoMatrix example for single NeoPixel Shield.
// Scrolls 'Howdy' across the matrix in a portrait (vertical) orientation.

#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#include <gfxfont.h>
#include "colorString.h"
#include "matrixsetup.h"
#include "colorPrinters.h"

#ifndef PSTR
 #define PSTR // Make Arduino Due happy
#endif

#define PIN 10
int blepin = 7;
int x = matrix.width();
int alarm;



//void add(char const *string,int colorMode,  rgb color);


void generateListElements(){
  add("JUGEND HACKT ss ", COLOR_MODE_HSV_RAINBOW, {});
  add("HAST DU NOCH NIE", COLOR_MODE_SINGLE, {200,200,0});
  add("EINEN HUT GESEHEN? ss ", COLOR_MODE_SINGLE, {0,200,200});
  add("PINK FLUFFY UNICORNS DANCING ON RAINBOWS ss ", COLOR_MODE_SINUS_RAINBOW,{});
}

colorString* firstListEl = NULL;
void add(char const *string,int colorMode,  rgb color){
  
  //create Element
  colorString* newListEl = (colorString*)malloc(sizeof(colorString));
  newListEl->string = string;
  newListEl->colorMode = colorMode;
  newListEl->color = color;
  newListEl->next = NULL;

  //add Element
  if (firstListEl == NULL)
  {
    firstListEl = newListEl;
  }
  else
  {
    //find last Element
    colorString* lastListEl = firstListEl;
    while(lastListEl->next!=NULL)
    {
      lastListEl=lastListEl->next;
    }
    lastListEl->next = newListEl;
  }

}


int printColorCodedText(){
  int length = 0;
  colorString* listElPointer = firstListEl;
  while(listElPointer){
    
    switch(listElPointer->colorMode){
      case 1:
        singleColor(listElPointer->string,listElPointer->color);
        break;
      case 2:
        sinusRainbow(listElPointer->string);
        break;
      case 3:
        hsvRainbow(listElPointer->string);
        break;
      case 4:
        rgbColor(listElPointer->string);
        break;
      case 5:
        randomColor(listElPointer->string);
        break;
      default:
        sinusRainbow(listElPointer->string);

    }
    
    length += strlen(listElPointer->string);
    listElPointer = listElPointer->next;
   
  }
  return length;
}



int pause(int str_len,int x){
  int pixlength=(str_len)*6;
  

  if(--x < (-pixlength)) {
    x = matrix.width();

  }
  return x;
}

int continuous(int str_len,int x){
  int pixlength=(str_len)*6;

  if(--x < -6*((int)strlen(firstListEl->string))) {

    x +=(int) 6*strlen(firstListEl->string);

   //find last Element
    colorString* lastListEl = firstListEl;
    while(lastListEl->next!=NULL)
    {
      lastListEl=lastListEl->next;
    }
    lastListEl->next = firstListEl;
    firstListEl = firstListEl->next;
    lastListEl->next->next =NULL;

  }
  return x;
}




void setup() {
  Serial.begin(115200);
  pinMode(blepin, INPUT);
  matrix.begin();
  matrix.setTextWrap(false);
  matrix.setBrightness(50);
  generateListElements();
  //matrix.setTextColor(colors[0]);
}

void loop() {

  matrix.fillScreen(1);
  matrix.setCursor(x, 0);
  alarm = digitalRead(blepin);
  if(blepin == LOW){
    //TODO ALLES ENTFERNEN
    add("ALARM", COLOR_MODE_SINGLE, {200,0,0});
    }
  int str_len = printColorCodedText();
  x = continuous(str_len,x);
  matrix.show();
  delay(75);
}
