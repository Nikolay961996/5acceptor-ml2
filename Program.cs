using System;

class Program
{
    static void Main(string[] args)
    {
        // Bad naming conventions and unclear purpose
        int a = 10;
        int b = 5;
        int c = a + b; // What is 'c'? Unclear variable names

        // Unnecessarily complex logic for a simple task
        if (c > 10)
        {
            Console.WriteLine("Greater than 10");
        }
        else if (c < 10)
        {
            Console.WriteLine("Less than 10");
        }
        else
        {
            Console.WriteLine("Equal to 10");
        }

        // Hardcoded values and magic numbers
        int[] arr = new int[5] { 1, 2, 3, 4, 5 };
        for (int i = 0; i < arr.Length; i++)
        {
            Console.WriteLine(arr[i]); // No context about what 'arr' represents
        }

        // No error handling or validation
        int x = Convert.ToInt32(Console.ReadLine()); // Could throw an exception if input is invalid

        // Unused variable and unnecessary complexity
        int unusedVariable = 0; // This variable is never used
        for (int j = 0; j < 100; j++)
        {
            unusedVariable += j; // This loop does something but the result is never used
        }

        // Lack of comments and documentation
        Console.WriteLine("Done"); // What does "Done" refer to?
    }
}