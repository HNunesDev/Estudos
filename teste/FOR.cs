// See https://aka.ms/new-console-template for more information
int x = int.Parse(Console.ReadLine());

for (int i = 1; i <= x; i++)
{
    if (i % 2 != 0)
    {
        Console.WriteLine(i);
    }
}