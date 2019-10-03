{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Py-Sock-Scanner.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "adbTva8n7IqG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 66
        },
        "outputId": "8dce27be-a340-4fdd-e580-60a807e38255"
      },
      "source": [
        "#!/usr/bin/env python\n",
        "import socket\n",
        "import subprocess\n",
        "import sys\n",
        "from datetime import datetime\n",
        "\n",
        "# Clear the screen\n",
        "subprocess.call('clear', shell=True)\n",
        "\n",
        "# Ask for input\n",
        "# Modified to take explicit input from code for future form input\n",
        "remoteServer = \"71.59.0.201\"\n",
        "remoteServerIP = socket.gethostbyname(remoteServer)\n",
        "\n",
        "# Print a nice banner with information on which host we are about to scan\n",
        "print(\"-\" * 60)\n",
        "print(\"Please wait, scanning remote host\", remoteServerIP)\n",
        "print(\"-\" * 60)\n",
        "\n",
        "# Check what time the scan started\n",
        "t1 = datetime.now()\n",
        "\n",
        "# Using the range function to specify ports (here it will scans all ports between 1 and 1024)\n",
        "\n",
        "# We also put in some error handling for catching errors\n",
        "\n",
        "try:\n",
        "    for port in range(1,65535):  \n",
        "        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
        "        result = sock.connect_ex((remoteServerIP, port))\n",
        "        if result == 0:\n",
        "            print(\"Port {}: \t Open\".format(port))\n",
        "        sock.close()\n",
        "\n",
        "except KeyboardInterrupt:\n",
        "    print(\"You pressed Ctrl+C\")\n",
        "    sys.exit()\n",
        "\n",
        "except socket.gaierror:\n",
        "    print('Hostname could not be resolved. Exiting')\n",
        "    sys.exit()\n",
        "\n",
        "except socket.error:\n",
        "    print(\"Couldn't connect to server\")\n",
        "    sys.exit()\n",
        "\n",
        "# Checking the time again\n",
        "t2 = datetime.now()\n",
        "\n",
        "# Calculates the difference of time, to see how long it took to run the script\n",
        "total =  t2 - t1\n",
        "\n",
        "# Printing the information to screen\n",
        "print('Scanning Completed in: ', total)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "------------------------------------------------------------\n",
            "Please wait, scanning remote host 71.59.0.201\n",
            "------------------------------------------------------------\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}