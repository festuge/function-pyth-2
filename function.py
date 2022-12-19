{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPBHOCqsI6Ml7fQd3D3X/u4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/festuge/function-pyth-2/blob/main/function.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1QGwXxo85cWI",
        "outputId": "e609dea3-bc17-4bbd-e15d-10a0321a959b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter name: claudi\n",
            "Enter age: 33\n",
            "what is your favorite number: 3\n",
            "claudi\n",
            "33\n",
            "3\n",
            "False\n",
            "name: claudi\n"
          ]
        }
      ],
      "source": [
        "name = input('Enter name: ')\n",
        "age = input('Enter age: ')\n",
        "number = input('what is your favorite number: ')\n",
        "has_a_pet = False\n",
        "print(name)\n",
        "print(age)\n",
        "print(number)\n",
        "print(has_a_pet)\n",
        "print(\"name: \" + str(name))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#functions\n",
        "# def name_of_function(parameter1, paremeter2, ...):\n",
        "#      function body here"
      ],
      "metadata": {
        "id": "IKHmNp8sFO3P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def square(number):\n",
        "  print(\"Welcome to the square function\")\n",
        "  squared = number**2\n",
        "  return number**2"
      ],
      "metadata": {
        "id": "uS3a17L29Meq"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "squared = square(5.5)\n",
        "print(squared)\n",
        "\n",
        "my_number = 6\n",
        "print(square(my_number))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5MiOHIMyIr65",
        "outputId": "1b769cdf-980a-4e59-a122-129adcb4e0b4"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the square function\n",
            "30.25\n",
            "Welcome to the square function\n",
            "36\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 1.\n",
        "Write a function to cube a number. Call this function passing test values to it and print the result.\n",
        "\n",
        "2. Write a function, say_hello which takes in a name variable and print out \"Hello name\". Say_hello(\"zach\") should print \"Hello zack\". Call this function passing test values to it and print the result."
      ],
      "metadata": {
        "id": "7d2CD0tAV2pM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def cube(number):\n",
        "  print(\"welcome to cube function\")\n",
        "  cubed = number**3\n",
        "  return cubed"
      ],
      "metadata": {
        "id": "BoVeRWSSV5Pz"
      },
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fat = cube(3)\n",
        "print(fat)\n",
        "kantas = 5\n",
        "print(cube(kantas))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yUtA-REWYN6W",
        "outputId": "77af1b87-7a9a-4af6-d637-20821f232a5d"
      },
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "welcome to cube function\n",
            "27\n",
            "welcome to cube function\n",
            "125\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 2"
      ],
      "metadata": {
        "id": "f3GMcEtLaKkg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def say_hello(name):\n",
        "  print('Hello', name)\n",
        "  "
      ],
      "metadata": {
        "id": "kji0EzO8ZrmH"
      },
      "execution_count": 62,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "say_hello('Claudi')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2vhyiiFKowrW",
        "outputId": "ff7b04cf-09d7-459f-fad9-f5e1e07f423c"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Claudi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "function that adds two numbers"
      ],
      "metadata": {
        "id": "Vb_ysyxWkee4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def add(num1, num2):\n",
        "  addition = num1+num2\n",
        "  return addition"
      ],
      "metadata": {
        "id": "7lyIwnZJjijs"
      },
      "execution_count": 107,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mine = add(2, 3)\n",
        "print(mine)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q8kXaRcbk3gC",
        "outputId": "b31ca575-93d7-4c5b-efe5-1658b945cc45"
      },
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def sub(num1, num2):\n",
        "  subn = num1-num2\n",
        "  return subn"
      ],
      "metadata": {
        "id": "KeCPnxkylAdY"
      },
      "execution_count": 105,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mine = sub(9, 3)\n",
        "print(mine)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EIVdgCJGly2u",
        "outputId": "cd4e6831-ff5d-42c7-f2b3-9195b443e5b3"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Lets calculate Joe's BMI (unit in meters and kgs)\n",
        "BMI = weight/height**2"
      ],
      "metadata": {
        "id": "SJykjpf5sMmu"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "commenting as we see on this code below is called the Docstring documentation"
      ],
      "metadata": {
        "id": "Vne20vYUwG_G"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_bmi(height, weight):\n",
        "  '''Calculates the BMI of an individual from their height and weight.'''\n",
        "  BMI = weight / height**2\n",
        "  return BMI"
      ],
      "metadata": {
        "id": "QhQVpSmms2sy"
      },
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "calculate_bmi(1.86, 111)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pf-_ujoFtxKb",
        "outputId": "70744360-a67e-4397-a24d-ac43cddc3dcc"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "32.08463406174124"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "height = 1.4\n",
        "weight = 80\n",
        "calculate_bmi(height, weight)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6AqzvCnyva7t",
        "outputId": "9f053edf-90cc-4eae-f58c-25f28d0ed0a2"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "40.81632653061225"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def two_times(num):\n",
        "  print(2*num)"
      ],
      "metadata": {
        "id": "RNv8eQ7Rt_Tc"
      },
      "execution_count": 75,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "two_times(34)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ukIymqMMyDuY",
        "outputId": "46facc13-5f9b-490e-9d4a-192b1a87cc4c"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "68\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Converting mini project1 into a function"
      ],
      "metadata": {
        "id": "N41VrGatzEsB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#p = num1\n",
        "#r = num2\n",
        "#n = num3\n",
        "def total_amount(num1, num2, num3):\n",
        "  return num1*((1+num2)**(num3/12))"
      ],
      "metadata": {
        "id": "azFCzRJPyGuc"
      },
      "execution_count": 103,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#p = 10000\n",
        "#r = 0.05\n",
        "#n = 36\n",
        "total_amount(10000, 0.05, 36)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Y_1ctQj0FjH",
        "outputId": "dde7e021-9fbc-4465-82fe-44ea40f9c843"
      },
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11576.250000000002"
            ]
          },
          "metadata": {},
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Alternative way"
      ],
      "metadata": {
        "id": "yuC2Xify6-gP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_amount_owed(p, r, n):\n",
        "  power = n/12\n",
        "  rate_sum = 1 + (r/100)\n",
        "  raised = rate_sum ** power\n",
        "  Total_amount = p * raised\n",
        "  return Total_amount"
      ],
      "metadata": {
        "id": "MEal4YUc7BEp"
      },
      "execution_count": 111,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "calculate_amount_owed(10000, 5, 36)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c1n0nElz7fip",
        "outputId": "daddc6ec-8c98-47cf-e0af-fd0d2babdcce"
      },
      "execution_count": 112,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11576.250000000002"
            ]
          },
          "metadata": {},
          "execution_count": 112
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let convert mini project 2 into a function\n",
        "A = pi radius **2"
      ],
      "metadata": {
        "id": "w9tKvMQ97pZR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def area(pi, r):\n",
        "  answer = pi * (r ** 2)\n",
        "  return answer"
      ],
      "metadata": {
        "id": "m_i_euTK7uun"
      },
      "execution_count": 126,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "area(3.14, 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wOVWS8P3-95z",
        "outputId": "10c4d980-f01a-46df-ca55-f170c2bce2b3"
      },
      "execution_count": 127,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "78.5"
            ]
          },
          "metadata": {},
          "execution_count": 127
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Assignment. Convert Assignment 1 and 2 into a function."
      ],
      "metadata": {
        "id": "UATL1vchAFbl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# C = F - 32 * (5/9)\n",
        "def celcius(f):\n",
        "  answer = (f - 32) * 5/9\n",
        "  return answer"
      ],
      "metadata": {
        "id": "NtRgcSDnAN6T"
      },
      "execution_count": 130,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "celcius(70)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iDovk0ZlBhZ8",
        "outputId": "ff60634f-5217-4eea-8694-1d9560fc8152"
      },
      "execution_count": 134,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "21.11111111111111"
            ]
          },
          "metadata": {},
          "execution_count": 134
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Assignment 2"
      ],
      "metadata": {
        "id": "Mgmo-aAfCZBV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# V=pir**2h\n",
        "def volume(pi, r, h):\n",
        "  answer = pi * (r ** 2) * h\n",
        "  return answer"
      ],
      "metadata": {
        "id": "QyS6UZC0BqxM"
      },
      "execution_count": 135,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "volume(3.14, 2, 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ISpGTigXDXU9",
        "outputId": "fcd260f0-ef83-42d5-a6f4-a03193e7712f"
      },
      "execution_count": 136,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "37.68"
            ]
          },
          "metadata": {},
          "execution_count": 136
        }
      ]
    }
  ]
}