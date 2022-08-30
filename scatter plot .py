{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "130ad642",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Matplotlib is building the font cache; this may take a moment.\n"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6c95dae3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#scatter plot\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a38776bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=np.arange(0,10)\n",
    "y=np.arange(0,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "74439880",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x,y,c=\"r\",marker='*')\n",
    "plt.xlabel(\"X axis\")\n",
    "plt.ylabel(\"Y axis\")\n",
    "plt.title('scatter plot using plotlib')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3b724a2",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
