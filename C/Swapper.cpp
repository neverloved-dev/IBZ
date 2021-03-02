#include<iostream>
#include<string>
#include<vector>


class Cipher {
private:
 char	alphabet[69] = { 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
		'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н',
		'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х',
		'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э',
		'Ю', 'ю', 'Я', 'я', '_', ',', '.' };

public:
	std::string GetMessage()
	{
		std::string text;
		std::cout << "Введите сообщение: ";
		std::cin >> text;
		return text;
	}
	std::string Enconde(std::string text, std::vector <int> nums)
	{ 
		
		int str_size = text.length();
		int i;
		int sector;
		int n;
		std::cout << "Enter the number of groups :";
		std::cin >> n;

		// Check if string can be divided in 
	// n equal parts 
		if (str_size % n != 0)
		{
			std::cout << "Invalid Input: String size";
			std::cout << " is not divisible by " + n;
			return;
		}

		// Calculate the size of parts to 
		// find the division points 
		sector = str_size / n;
		
		for (i = 0; i < str_size; i++)
		{
			for (int pos = 0; pos < sector; pos++)
			{
				if (pos == sector)
				{
					sector -= pos;
					pos = 0;
					continue;
				}
				std::swap(text[pos], text[nums[i]]); // Swapping the charachters by their index
			}
		}

		return text;
	}
	std::string Decode(std::string text, std::vector <int> nums)
	{
		int str_size = text.length();
		int i;
		int sector;
		int n;
		std::cout << "Enter the number of groups :";
		std::cin >> n;

		// Check if string can be divided in 
	// n equal parts 
		if (str_size % n != 0)
		{
			std::cout << "Invalid Input: String size";
			std::cout << " is not divisible by " + n;
			return;
		}

		// Calculate the size of parts to 
		// find the division points 
		sector = str_size / n;
		
		std::reverse(nums.begin(), nums.end()); // Reversing the vector

		for (i = 0; i < str_size; i++)
		{
			for (int pos = 0; pos < sector; pos++)
			{
				if (pos == sector)
				{
					sector -= pos;
					pos = 0;
					continue;
				}
				std::swap(text[pos], text[nums[i]]); // Swapping the charachters by their index
			}
		}

		return text;
	}

	std::vector<int> GetKey()
	{
		int num;
		std::vector<int> input;
		std::cout << "Enter the key values. Upon entering 0 process will terminate"<<std::endl;
		while (std::cin>>num)
		{
			input.push_back(num);
		}


		return input;
	}
};

int main()
{
	Cipher cipher;
	std::string message;
	message = cipher.GetMessage();
	char choice;
	std::vector<int>Key;
	std::cout << "Encode or Decode ? : ";
	std::cin >> choice;
	Key = cipher.GetKey();
	if (choice == 'D' || choice == 'd')
		cipher.Decode(message, Key);
	if (choice == 'E' || choice == 'e')
		cipher.Enconde(message, Key);
}