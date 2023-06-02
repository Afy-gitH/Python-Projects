{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5beac6fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def guess(x):\n",
    "    random_number = random.randint(1,x)\n",
    "    guess = 0\n",
    "    while guess != random_number:\n",
    "        guess = int(input(f 'guess a number between 1 and {x}: '))\n",
    "        if guess < random_number:\n",
    "            print(\"Sorry, guess again. Too low\")\n",
    "        elif guess < random_number:\n",
    "            print(\"Sorry, guess again. Too Big\")\n",
    "            \n",
    "guess(int(input(\"input the upper limit : \")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25868558",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
