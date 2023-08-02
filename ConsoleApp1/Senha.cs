int senha = 2002;

Console.Write("Insira a senha para acessar: ");
int senhaUsuario = int.Parse(Console.ReadLine());

while (senhaUsuario != senha)
{
    Console.WriteLine("Senha invalida, tente novamente: ");
    senhaUsuario = int.Parse(Console.ReadLine());
}
Console.WriteLine("Acesso liberado!");