using System;
using System.Collections.Generic;

public static class Arrays
{
    public static double[] MultiplesOf(double number, int length)
    {
        // My thought process:
        // I want to return an array that contains multiples of a given number
        // For example, if the number is 3 and I want 5 multiples, I should get: 3, 6, 9, 12, 15
        // So I'll create an array with the correct length and fill it step-by-step

        double[] result = new double[length]; // Make space for the result values

        // Loop from 0 to (length - 1) so I can multiply the number by 1, 2, 3, etc
        for (int i = 0; i < length; i++)
        {
            result[i] = number * (i + 1); // (i + 1) so I don’t include 0 in the result
        }

        return result; // Return the filled array of multiples
    }

    public static void RotateListRight(List<int> data, int amount)
    {
        // Here's how I approached this:
        // I want to rotate the list to the right by a certain number of steps
        // That means the last 'amount' of elements should move to the front
        // For example, if the list is 1 to 9 and I rotate by 3, I expect 7, 8, 9 at the front

        amount %= data.Count; // This is to make sure the amount doesn't go beyond the size of the list

        // If the rotation amount is 0, there's nothing to change
        if (amount == 0)
        {
            return;
        }

        // Figure out where the "cut" happens—this is where the rotated part starts
        int start = data.Count - amount;

        // Take the last few elements I want to move
        List<int> tail = data.GetRange(start, amount);

        // Remove them from the end of the list
        data.RemoveRange(start, amount);

        // Add them back to the front of the list
        data.InsertRange(0, tail);
    }
}
