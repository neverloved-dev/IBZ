#include <iostream>
#include <string.h>
#include<clocale>

class Cipher
{
private:
	std::string message;
	int key;

public:
	char alphabet[36] = { 'а','б','в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
	'р','с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь','э','ю','я','_','.',',' };
	
	/// <summary>
	/// Getters and setters
	std::string GetMessage()
	{
		return message;
	}

	int GetKey()
	{
		return key;
	}

	std::string SetMessage(std::string NewMessage)
	{
		message = NewMessage;
		return message;
	}

	int SetKey(int aKey)
	{
		key = aKey;
		return key;
	}
	/// </summary>
	/// <returns> Ключь и сообщение </returns>
	Cipher(int keys, std::string Message)
	{
		SetKey(keys);
		SetMessage(Message);
	}

	std::string AdditCipher(int value,std::string Message)
	{
		std::string ciphred;
		char simbol;
		for (int i = 0; i < Message.length(); i++)
		{
			simbol = Message.at(i);
			for (int j = 0; j <sizeof(alphabet); j++)
			{
				if (simbol == alphabet[j])
				{
					simbol = alphabet[j + value];
					ciphred.push_back(simbol);
					if (ciphred.length() == Message.length())
					{
						return ciphred;
					}
				}
			}
		}		
	}

	std::string MultiCipher(int value, std::string Message)
	{
		std::string ciphred;
		char simbol;
		for (int i = 0; i < Message.length(); i++)
		{
			simbol = Message.at(i);
			for (int j = 0; j < sizeof(alphabet); j++)
			{
				if (simbol == alphabet[j])
				{
					simbol = alphabet[j * value];
					ciphred.push_back(simbol);
					if (ciphred.length() == Message.length())
					{
						return ciphred;
					}
				}
			}
		}
	}

	std::string AdditiveDeciphre(int value, std::string Message)
	{
		std::string ciphred;
		char simbol;
		for (int i = 0; i < Message.length(); i++)
		{
			simbol = Message.at(i);
			for (int j = 0; j < sizeof(alphabet); j++)
			{
				if (simbol == alphabet[j])
				{
					if (j == 0||j==36) //first simbol or last simbol of the array
						continue;
					simbol = alphabet[j - value];
					ciphred.push_back(simbol);
					if (ciphred.length() == Message.length())
					{
						return ciphred;
					}
				}
			}
		}
	}
	std::string MulitplDecipher(int value, std::string Message)
	{
		std::string ciphred;
		char simbol;
		for (int i = 0; i < Message.length(); i++)
		{
			simbol = Message.at(i);
			for (int j = 0; j < sizeof(alphabet); j++)
			{
				if (simbol == alphabet[j])
				{
					if (j == 0 || j == 36) //first simbol or last simbol of the array
						continue;
					simbol = alphabet[j /value]; 
					ciphred.push_back(simbol);
					if (ciphred.length() == Message.length())
					{
						return ciphred;
					}
				}
			}
		}
	}
};

int main()
{
	setlocale(LC_ALL, "Russian");
	int userKey;
	std::string userMesage;

	std::cout << "Введите длину ключа : ";
	std::cin >> userKey;

	while(userMesage.empty())
	{
		std::cout << "Введите сообщение (количество символов не должно быть больше значения ключа) :" << std::endl;
		std::cin >> userMesage;
	}

	Cipher sifra = Cipher(userKey,userMesage);
	std::cout << "Additive Chiper" << std::endl;
	std::string addCipher = sifra.AdditCipher(userKey,userMesage);
	std::cout << addCipher+"\n";
	std::cout << "Multiplicative Cipher" << std::endl;
	std::string multiCipher = sifra.MultiCipher(userKey, userMesage);
	std::cout << multiCipher+"\n";
	
}