module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);
        void printRepeat(string s, int count);
    }

    interface Calculator
    {
        int add(int a, int b);
        int multiply(int a, int b);
    }
}
