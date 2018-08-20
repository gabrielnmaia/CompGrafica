void setup() 
{
  size(500, 500);
 
}

void draw()
{
  background(200);
 
  float r = min(width, height) * 0.45;
  float cx = width / 2;
  float cy = height / 2;
  
  translate(cx, cy);
  fill(255);  
  ellipse(0, 0, 2 * r, 2 * r);

  float tt = 20;
  float tm = 10;

  for(int i = 0; i < 60; i++)
  {
    float alpha = i * PI / 30 - HALF_PI;
    float x = cos(alpha);
    float y = sin(alpha);
     
    if(i % 5 != 0)
    { 
      line(x * (r - tm), y * (r - tm), x * r, y * r);
    }
    else
    {
      fill(0);
  
      if(i == 0)
      {
       text("12", x * (r - tt), y * (r - tt));
      }
      else
      {
         text((i / 5) + "", x * (r - tt), y * (r - tt));
      }

      line(x * (r - tt), y * (r - tt), x * r, y * r);
    }
    
    float minuto_alpha = (i + (second() / 60.0)) * PI / 30 - HALF_PI;
    float minuto_x = cos(minuto_alpha);
    float minuto_y = sin(minuto_alpha);
    
    float hora_alpha = (i + (5 * (minute() / 60.0))) * PI / 30 - HALF_PI;
    float hora_x = cos(hora_alpha);
    float hora_y = sin(hora_alpha);
    
    if((hour() % 12) * 5 == i)
    {
      line(hora_x, hora_y, hora_x * (r * 0.55), hora_y * (r * 0.55));
    }
    if(minute() == i) 
    {
      line(minuto_x, minuto_y, minuto_x * (r * 0.8), minuto_y * (r * 0.8));   
    }
    if(second() == i) 
    {
      line(x, y, x * (r * 0.7), y * (r * 0.7));
      
    }
  }
}
