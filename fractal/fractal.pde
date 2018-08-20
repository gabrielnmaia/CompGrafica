float[] rodar(float cx, float cy, float px, float py, float a)
{
  float _px = ((px - cx) * cos(a) - (py - cy) * sin(a)) + cx;
  float _py = ((px - cx) * sin(a) + (py - cy) * cos(a)) + cy;
  
  return new float[] { _px, _py };
}

void koch(float ax, float ay, float bx, float by, float n)
{
  if(n == 0)
  {
    line(ax, ay, bx, by); 
  }
  else
  {
    float cx = ax + (1.0/3 * (bx - ax));
    float cy = ay + (1.0/3 * (by - ay));
    float dx = ax + (2.0/3 * (bx - ax));
    float dy = ay + (2.0/3 * (by - ay));
    float e[] = rodar(cx, cy, dx, dy, - PI / 3);

    koch(ax, ay, cx, cy, n - 1);
    koch(cx, cy, e[0], e[1], n - 1);
    koch(e[0], e[1], dx, dy, n - 1);
    koch(dx, dy, bx, by, n - 1);
  }
}

void setup()
{
   size(800, 600);
}

void draw()
{
  background(200);
  
  int   n = 3;
  float r = min(width, height) * 0.45;
  float cx = width / 2;
  float cy = height / 2;

  translate(cx, cy);
  fill(255);

  for(int i = 0; i < n; i++)
  {
    float alpha1 = i * PI / (n / 2.0) - HALF_PI;
    float alpha2 = ((i != n - 1) ? i + 1 : 0) * PI / (n / 2.0) - HALF_PI;
   
    float x1 = cos(alpha1);
    float y1 = sin(alpha1);
    float x2 = cos(alpha2);
    float y2 = sin(alpha2);
    
    koch(x1 * r, y1 * r, x2 * r, y2 * r, 8 * mouseX / width);
  }
}
