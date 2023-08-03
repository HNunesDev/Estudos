Console.Write("Quantos números inteiros você vai digitar? ");
int N = int.Parse(Console.ReadLine());

int soma = 0;
for (int i = 1; i <= N; i++)
{
    Console.Write("Digite seu número: ");
    int n1 = int.Parse(Console.ReadLine());
    soma = soma + n1;
}
Console.WriteLine(soma);