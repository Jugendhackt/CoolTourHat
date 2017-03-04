void hsvRainbow(const char* string){

  for(int i=0; i<strlen(string);i++){

    
    rgb color = HSVColor((i*21)%360,1,1);
    matrix.setTextColor(matrix.Color(color.r*255,color.g*255,color.b*255));
    matrix.print(string[i]);
  }
}
void sinusRainbow(const char* string){

  for(int i=0; i<strlen(string);i++){

    matrix.setTextColor(matrix.Color(sin(i*0.2)*128+127, sin(i*0.2+PI)*128+127, sin(i*0.2 + PI/2)*128+127));
    matrix.print(string[i]);
  }
}
void rgbColor(const char* string){
  const uint16_t colors[] = {
    matrix.Color(255, 0, 0), matrix.Color(0, 255, 0), matrix.Color(0, 0, 255) };

  for(int i=0; i<strlen(string);i++){

    //matrix.setTextColor(colors[i%3]);
    matrix.setTextColor(colors[i%3]);
    matrix.print(string[i]);
  }
}
void randomColor(const char* string){
  const uint16_t colors[] = {
    matrix.Color(255, 0, 0), matrix.Color(0, 255, 0), matrix.Color(0, 0, 255) };

  for(int i=0; i<strlen(string);i++){

    //matrix.setTextColor(colors[i%3]);
    matrix.setTextColor(matrix.Color(random(0,255),random(0,255), random(0,255)));
    matrix.print(string[i]);
  }
}


void singleColor(const char* string, rgb color){
  matrix.setTextColor(matrix.Color(color.r,color.g, color.b));
  for(int i=0; i<strlen(string);i++){
    matrix.print(string[i]);
  }
}
