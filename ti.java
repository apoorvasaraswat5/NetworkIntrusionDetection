class Tiger
{
 int leg=4;
 static int eyes=2;
 void liftTree()
  { 
    System.out.println("ABC");
  }
 static void foldTree()
  { 
   System.out.println("XYZ");
  }
 static
 { 
  System.out.println("static block");
 }
 {
  System.out.println("non-static block");
 }
public static void main(String...args) 
 {
  System.out.println("Main method");
  Tiger t= new Tiger();
  t.liftTree();
  System.out.println("leg="+t.leg);
  System.out.println("eyes="+eyes);
 }
}
 