{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8ef5adb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import cv2\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5d1ed764",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "data_dir = os.path.join(os.getcwd(),'clean_data')\n",
    "\n",
    "img_dir = os.path.join(os.getcwd(),'images')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "318c0684",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\USER\\\\Desktop\\\\AI AND ML\\\\project\\\\AI_ML PROJECT'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "47752462",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess(image):\n",
    "    image = cv2.resize(image,(100,100))\n",
    "    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)\n",
    "    return image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f16ee0e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "images = []\n",
    "labels = []\n",
    "\n",
    "for i in os.listdir(img_dir):\n",
    "    image = cv2.imread(os.path.join(img_dir,i))\n",
    "    image = preprocess(image)\n",
    "    images.append(image)\n",
    "    labels.append(i.split('_')[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "356d2c5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mona_1 - Copy (2).jpg', 'mona_1 - Copy.jpg', 'mona_1.jpg', 'mona_10 - Copy (2).jpg', 'mona_10 - Copy.jpg', 'mona_10.jpg', 'mona_100 - Copy (2).jpg', 'mona_100 - Copy.jpg', 'mona_100.jpg', 'mona_11 - Copy (2).jpg', 'mona_11 - Copy.jpg', 'mona_11.jpg', 'mona_12 - Copy (2).jpg', 'mona_12 - Copy.jpg', 'mona_12.jpg', 'mona_13 - Copy (2).jpg', 'mona_13 - Copy.jpg', 'mona_13.jpg', 'mona_15 - Copy (2).jpg', 'mona_15 - Copy.jpg', 'mona_15.jpg', 'mona_17 - Copy (2).jpg', 'mona_17 - Copy.jpg', 'mona_17.jpg', 'mona_18 - Copy (2).jpg', 'mona_18 - Copy.jpg', 'mona_18.jpg', 'mona_19 - Copy (2).jpg', 'mona_19 - Copy.jpg', 'mona_19.jpg', 'mona_2 - Copy (2).jpg', 'mona_2 - Copy.jpg', 'mona_2.jpg', 'mona_20 - Copy (2).jpg', 'mona_20 - Copy.jpg', 'mona_20.jpg', 'mona_21 - Copy (2).jpg', 'mona_21 - Copy.jpg', 'mona_21.jpg', 'mona_22 - Copy (2).jpg', 'mona_22 - Copy.jpg', 'mona_22.jpg', 'mona_23 - Copy (2).jpg', 'mona_23 - Copy.jpg', 'mona_23.jpg', 'mona_24 - Copy (2).jpg', 'mona_24 - Copy.jpg', 'mona_24.jpg', 'mona_25 - Copy (2).jpg', 'mona_25 - Copy.jpg', 'mona_25.jpg', 'mona_26 - Copy (2).jpg', 'mona_26 - Copy.jpg', 'mona_26.jpg', 'mona_27 - Copy (2).jpg', 'mona_27 - Copy.jpg', 'mona_27.jpg', 'mona_28 - Copy (2).jpg', 'mona_28 - Copy.jpg', 'mona_28.jpg', 'mona_29 - Copy (2).jpg', 'mona_29 - Copy.jpg', 'mona_29.jpg', 'mona_3 - Copy (2).jpg', 'mona_3 - Copy.jpg', 'mona_3.jpg', 'mona_30 - Copy (2).jpg', 'mona_30 - Copy.jpg', 'mona_30.jpg', 'mona_31 - Copy (2).jpg', 'mona_31 - Copy.jpg', 'mona_31.jpg', 'mona_32 - Copy (2).jpg', 'mona_32 - Copy.jpg', 'mona_32.jpg', 'mona_33 - Copy (2).jpg', 'mona_33 - Copy.jpg', 'mona_33.jpg', 'mona_34 - Copy (2).jpg', 'mona_34 - Copy.jpg', 'mona_34.jpg', 'mona_35 - Copy (2).jpg', 'mona_35 - Copy.jpg', 'mona_35.jpg', 'mona_36 - Copy (2).jpg', 'mona_36 - Copy.jpg', 'mona_36.jpg', 'mona_37 - Copy (2).jpg', 'mona_37 - Copy.jpg', 'mona_37.jpg', 'mona_38 - Copy (2).jpg', 'mona_38 - Copy.jpg', 'mona_38.jpg', 'mona_39 - Copy (2).jpg', 'mona_39 - Copy.jpg', 'mona_39.jpg', 'mona_4 - Copy (2).jpg', 'mona_4 - Copy.jpg', 'mona_4.jpg', 'mona_40 - Copy (2).jpg', 'mona_40 - Copy.jpg', 'mona_40.jpg', 'mona_41 - Copy (2).jpg', 'mona_41 - Copy.jpg', 'mona_41.jpg', 'mona_42 - Copy (2).jpg', 'mona_42 - Copy.jpg', 'mona_42.jpg', 'mona_43 - Copy (2).jpg', 'mona_43 - Copy.jpg', 'mona_43.jpg', 'mona_44 - Copy (2).jpg', 'mona_44 - Copy.jpg', 'mona_44.jpg', 'mona_45 - Copy (2).jpg', 'mona_45 - Copy.jpg', 'mona_45.jpg', 'mona_46 - Copy (2).jpg', 'mona_46 - Copy.jpg', 'mona_46.jpg', 'mona_47 - Copy (2).jpg', 'mona_47 - Copy.jpg', 'mona_47.jpg', 'mona_48 - Copy (2).jpg', 'mona_48 - Copy.jpg', 'mona_48.jpg', 'mona_49 - Copy (2).jpg', 'mona_49 - Copy.jpg', 'mona_49.jpg', 'mona_5 - Copy (2).jpg', 'mona_5 - Copy.jpg', 'mona_5.jpg', 'mona_50 - Copy (2).jpg', 'mona_50 - Copy.jpg', 'mona_50.jpg', 'mona_51 - Copy (2).jpg', 'mona_51 - Copy.jpg', 'mona_51.jpg', 'mona_52 - Copy (2).jpg', 'mona_52 - Copy.jpg', 'mona_52.jpg', 'mona_53 - Copy (2).jpg', 'mona_53 - Copy.jpg', 'mona_53.jpg', 'mona_54 - Copy (2).jpg', 'mona_54 - Copy.jpg', 'mona_54.jpg', 'mona_55 - Copy (2).jpg', 'mona_55 - Copy.jpg', 'mona_55.jpg', 'mona_56 - Copy (2).jpg', 'mona_56 - Copy.jpg', 'mona_56.jpg', 'mona_57 - Copy (2).jpg', 'mona_57 - Copy.jpg', 'mona_57.jpg', 'mona_58 - Copy (2).jpg', 'mona_58 - Copy.jpg', 'mona_58.jpg', 'mona_59 - Copy (2).jpg', 'mona_59 - Copy.jpg', 'mona_59.jpg', 'mona_6 - Copy (2).jpg', 'mona_6 - Copy.jpg', 'mona_6.jpg', 'mona_60 - Copy (2).jpg', 'mona_60 - Copy.jpg', 'mona_60.jpg', 'mona_61 - Copy (2).jpg', 'mona_61 - Copy.jpg', 'mona_61.jpg', 'mona_62 - Copy (2).jpg', 'mona_62 - Copy.jpg', 'mona_62.jpg', 'mona_63 - Copy (2).jpg', 'mona_63 - Copy.jpg', 'mona_63.jpg', 'mona_64 - Copy (2).jpg', 'mona_64 - Copy.jpg', 'mona_64.jpg', 'mona_65 - Copy (2).jpg', 'mona_65 - Copy.jpg', 'mona_65.jpg', 'mona_66 - Copy (2).jpg', 'mona_66 - Copy.jpg', 'mona_66.jpg', 'mona_67 - Copy (2).jpg', 'mona_67 - Copy.jpg', 'mona_67.jpg', 'mona_68 - Copy (2).jpg', 'mona_68 - Copy.jpg', 'mona_68.jpg', 'mona_69 - Copy (2).jpg', 'mona_69 - Copy.jpg', 'mona_69.jpg', 'mona_7 - Copy (2).jpg', 'mona_7 - Copy.jpg', 'mona_7.jpg', 'mona_70 - Copy (2).jpg', 'mona_70 - Copy.jpg', 'mona_70.jpg', 'mona_71 - Copy (2).jpg', 'mona_71 - Copy.jpg', 'mona_71.jpg', 'mona_72 - Copy (2).jpg', 'mona_72 - Copy.jpg', 'mona_72.jpg', 'mona_73 - Copy (2).jpg', 'mona_73 - Copy.jpg', 'mona_73.jpg', 'mona_74 - Copy (2).jpg', 'mona_74 - Copy.jpg', 'mona_74.jpg', 'mona_75 - Copy (2).jpg', 'mona_75 - Copy.jpg', 'mona_75.jpg', 'mona_76 - Copy (2).jpg', 'mona_76 - Copy.jpg', 'mona_76.jpg', 'mona_77 - Copy (2).jpg', 'mona_77 - Copy.jpg', 'mona_77.jpg', 'mona_78 - Copy (2).jpg', 'mona_78 - Copy.jpg', 'mona_78.jpg', 'mona_79 - Copy (2).jpg', 'mona_79 - Copy.jpg', 'mona_79.jpg', 'mona_8 - Copy (2).jpg', 'mona_8 - Copy.jpg', 'mona_8.jpg', 'mona_80 - Copy (2).jpg', 'mona_80 - Copy.jpg', 'mona_80.jpg', 'mona_81 - Copy (2).jpg', 'mona_81 - Copy.jpg', 'mona_81.jpg', 'mona_82 - Copy (2).jpg', 'mona_82 - Copy.jpg', 'mona_82.jpg', 'mona_83 - Copy (2).jpg', 'mona_83 - Copy.jpg', 'mona_83.jpg', 'mona_84 - Copy (2).jpg', 'mona_84 - Copy.jpg', 'mona_84.jpg', 'mona_85 - Copy (2).jpg', 'mona_85 - Copy.jpg', 'mona_85.jpg', 'mona_86 - Copy (2).jpg', 'mona_86 - Copy.jpg', 'mona_86.jpg', 'mona_87 - Copy (2).jpg', 'mona_87 - Copy.jpg', 'mona_87.jpg', 'mona_88 - Copy (2).jpg', 'mona_88 - Copy.jpg', 'mona_88.jpg', 'mona_89 - Copy (2).jpg', 'mona_89 - Copy.jpg', 'mona_89.jpg', 'mona_9 - Copy (2).jpg', 'mona_9 - Copy.jpg', 'mona_9.jpg', 'mona_90 - Copy (2).jpg', 'mona_90 - Copy.jpg', 'mona_90.jpg', 'mona_91 - Copy (2).jpg', 'mona_91 - Copy.jpg', 'mona_91.jpg', 'mona_92 - Copy (2).jpg', 'mona_92 - Copy.jpg', 'mona_92.jpg', 'mona_93 - Copy (2).jpg', 'mona_93 - Copy.jpg', 'mona_93.jpg', 'mona_94 - Copy (2).jpg', 'mona_94 - Copy.jpg', 'mona_94.jpg', 'mona_95 - Copy (2).jpg', 'mona_95 - Copy.jpg', 'mona_95.jpg', 'mona_96 - Copy (2).jpg', 'mona_96 - Copy.jpg', 'mona_96.jpg', 'mona_97 - Copy (2).jpg', 'mona_97 - Copy.jpg', 'mona_97.jpg', 'mona_98 - Copy (2).jpg', 'mona_98 - Copy.jpg', 'mona_98.jpg', 'mona_99 - Copy (2).jpg', 'mona_99 - Copy.jpg', 'mona_99.jpg', 'priyanka_1 - Copy (2).jpg', 'priyanka_1 - Copy.jpg', 'priyanka_1.jpg', 'priyanka_100 - Copy (2).jpg', 'priyanka_100 - Copy.jpg', 'priyanka_100.jpg', 'priyanka_11 - Copy (2).jpg', 'priyanka_11 - Copy.jpg', 'priyanka_11.jpg', 'priyanka_12 - Copy (2).jpg', 'priyanka_12 - Copy.jpg', 'priyanka_12.jpg', 'priyanka_13 - Copy (2).jpg', 'priyanka_13 - Copy.jpg', 'priyanka_13.jpg', 'priyanka_14 - Copy (2).jpg', 'priyanka_14 - Copy.jpg', 'priyanka_14.jpg', 'priyanka_15 - Copy (2).jpg', 'priyanka_15 - Copy.jpg', 'priyanka_15.jpg', 'priyanka_17 - Copy (2).jpg', 'priyanka_17 - Copy.jpg', 'priyanka_17.jpg', 'priyanka_18 - Copy (2).jpg', 'priyanka_18 - Copy.jpg', 'priyanka_18.jpg', 'priyanka_19 - Copy (2).jpg', 'priyanka_19 - Copy.jpg', 'priyanka_19.jpg', 'priyanka_2 - Copy (2).jpg', 'priyanka_2 - Copy.jpg', 'priyanka_2.jpg', 'priyanka_20 - Copy (2).jpg', 'priyanka_20 - Copy.jpg', 'priyanka_20.jpg', 'priyanka_21 - Copy (2).jpg', 'priyanka_21 - Copy.jpg', 'priyanka_21.jpg', 'priyanka_22 - Copy (2).jpg', 'priyanka_22 - Copy.jpg', 'priyanka_22.jpg', 'priyanka_23 - Copy (2).jpg', 'priyanka_23 - Copy.jpg', 'priyanka_23.jpg', 'priyanka_25 - Copy (2).jpg', 'priyanka_25 - Copy.jpg', 'priyanka_25.jpg', 'priyanka_26 - Copy (2).jpg', 'priyanka_26 - Copy.jpg', 'priyanka_26.jpg', 'priyanka_27 - Copy (2).jpg', 'priyanka_27 - Copy.jpg', 'priyanka_27.jpg', 'priyanka_28 - Copy (2).jpg', 'priyanka_28 - Copy.jpg', 'priyanka_28.jpg', 'priyanka_30 - Copy (2).jpg', 'priyanka_30 - Copy.jpg', 'priyanka_30.jpg', 'priyanka_31 - Copy (2).jpg', 'priyanka_31 - Copy.jpg', 'priyanka_31.jpg', 'priyanka_32 - Copy (2).jpg', 'priyanka_32 - Copy.jpg', 'priyanka_32.jpg', 'priyanka_34 - Copy (2).jpg', 'priyanka_34 - Copy.jpg', 'priyanka_34.jpg', 'priyanka_35 - Copy (2).jpg', 'priyanka_35 - Copy.jpg', 'priyanka_35.jpg', 'priyanka_36 - Copy (2).jpg', 'priyanka_36 - Copy.jpg', 'priyanka_36.jpg', 'priyanka_37 - Copy (2).jpg', 'priyanka_37 - Copy.jpg', 'priyanka_37.jpg', 'priyanka_38 - Copy (2).jpg', 'priyanka_38 - Copy.jpg', 'priyanka_38.jpg', 'priyanka_39 - Copy (2).jpg', 'priyanka_39 - Copy.jpg', 'priyanka_39.jpg', 'priyanka_4 - Copy (2).jpg', 'priyanka_4 - Copy.jpg', 'priyanka_4.jpg', 'priyanka_40 - Copy (2).jpg', 'priyanka_40 - Copy.jpg', 'priyanka_40.jpg', 'priyanka_41 - Copy (2).jpg', 'priyanka_41 - Copy.jpg', 'priyanka_41.jpg', 'priyanka_42 - Copy (2).jpg', 'priyanka_42 - Copy.jpg', 'priyanka_42.jpg', 'priyanka_43 - Copy (2).jpg', 'priyanka_43 - Copy.jpg', 'priyanka_43.jpg', 'priyanka_44 - Copy (2).jpg', 'priyanka_44 - Copy.jpg', 'priyanka_44.jpg', 'priyanka_45 - Copy (2).jpg', 'priyanka_45 - Copy.jpg', 'priyanka_45.jpg', 'priyanka_47 - Copy (2).jpg', 'priyanka_47 - Copy.jpg', 'priyanka_47.jpg', 'priyanka_48 - Copy (2).jpg', 'priyanka_48 - Copy.jpg', 'priyanka_48.jpg', 'priyanka_49 - Copy (2).jpg', 'priyanka_49 - Copy.jpg', 'priyanka_49.jpg', 'priyanka_5 - Copy (2).jpg', 'priyanka_5 - Copy.jpg', 'priyanka_5.jpg', 'priyanka_50 - Copy (2).jpg', 'priyanka_50 - Copy.jpg', 'priyanka_50.jpg', 'priyanka_52 - Copy (2).jpg', 'priyanka_52 - Copy.jpg', 'priyanka_52.jpg', 'priyanka_53 - Copy (2).jpg', 'priyanka_53 - Copy.jpg', 'priyanka_53.jpg', 'priyanka_54 - Copy (2).jpg', 'priyanka_54 - Copy.jpg', 'priyanka_54.jpg', 'priyanka_55 - Copy (2).jpg', 'priyanka_55 - Copy.jpg', 'priyanka_55.jpg', 'priyanka_56 - Copy (2).jpg', 'priyanka_56 - Copy.jpg', 'priyanka_56.jpg', 'priyanka_57 - Copy (2).jpg', 'priyanka_57 - Copy.jpg', 'priyanka_57.jpg', 'priyanka_58 - Copy (2).jpg', 'priyanka_58 - Copy.jpg', 'priyanka_58.jpg', 'priyanka_59 - Copy (2).jpg', 'priyanka_59 - Copy.jpg', 'priyanka_59.jpg', 'priyanka_6 - Copy (2).jpg', 'priyanka_6 - Copy.jpg', 'priyanka_6.jpg', 'priyanka_60 - Copy (2).jpg', 'priyanka_60 - Copy.jpg', 'priyanka_60.jpg', 'priyanka_61 - Copy (2).jpg', 'priyanka_61 - Copy.jpg', 'priyanka_61.jpg', 'priyanka_63 - Copy (2).jpg', 'priyanka_63 - Copy.jpg', 'priyanka_63.jpg', 'priyanka_64 - Copy (2).jpg', 'priyanka_64 - Copy.jpg', 'priyanka_64.jpg', 'priyanka_65 - Copy (2).jpg', 'priyanka_65 - Copy.jpg', 'priyanka_65.jpg', 'priyanka_66 - Copy (2).jpg', 'priyanka_66 - Copy.jpg', 'priyanka_66.jpg', 'priyanka_67 - Copy (2).jpg', 'priyanka_67 - Copy.jpg', 'priyanka_67.jpg', 'priyanka_68 - Copy (2).jpg', 'priyanka_68 - Copy.jpg', 'priyanka_68.jpg', 'priyanka_69 - Copy (2).jpg', 'priyanka_69 - Copy.jpg', 'priyanka_69.jpg', 'priyanka_7 - Copy (2).jpg', 'priyanka_7 - Copy.jpg', 'priyanka_7.jpg', 'priyanka_71 - Copy (2).jpg', 'priyanka_71 - Copy.jpg', 'priyanka_71.jpg', 'priyanka_74 - Copy (2).jpg', 'priyanka_74 - Copy.jpg', 'priyanka_74.jpg', 'priyanka_75 - Copy (2).jpg', 'priyanka_75 - Copy.jpg', 'priyanka_75.jpg', 'priyanka_76 - Copy (2).jpg', 'priyanka_76 - Copy.jpg', 'priyanka_76.jpg', 'priyanka_78 - Copy (2).jpg', 'priyanka_78 - Copy.jpg', 'priyanka_78.jpg', 'priyanka_8 - Copy (2).jpg', 'priyanka_8 - Copy.jpg', 'priyanka_8.jpg', 'priyanka_80 - Copy (2).jpg', 'priyanka_80 - Copy.jpg', 'priyanka_80.jpg', 'priyanka_81 - Copy (2).jpg', 'priyanka_81 - Copy.jpg', 'priyanka_81.jpg', 'priyanka_83 - Copy (2).jpg', 'priyanka_83 - Copy.jpg', 'priyanka_83.jpg', 'priyanka_84 - Copy (2).jpg', 'priyanka_84 - Copy.jpg', 'priyanka_84.jpg', 'priyanka_85 - Copy (2).jpg', 'priyanka_85 - Copy.jpg', 'priyanka_85.jpg', 'priyanka_86 - Copy (2).jpg', 'priyanka_86 - Copy.jpg', 'priyanka_86.jpg', 'priyanka_87 - Copy (2).jpg', 'priyanka_87 - Copy.jpg', 'priyanka_87.jpg', 'priyanka_88 - Copy (2).jpg', 'priyanka_88 - Copy.jpg', 'priyanka_88.jpg', 'priyanka_89 - Copy (2).jpg', 'priyanka_89 - Copy.jpg', 'priyanka_89.jpg', 'priyanka_9 - Copy (2).jpg', 'priyanka_9 - Copy.jpg', 'priyanka_9.jpg', 'priyanka_90 - Copy (2).jpg', 'priyanka_90 - Copy.jpg', 'priyanka_90.jpg', 'priyanka_91 - Copy (2).jpg', 'priyanka_91 - Copy.jpg', 'priyanka_91.jpg', 'priyanka_92 - Copy (2).jpg', 'priyanka_92 - Copy.jpg', 'priyanka_92.jpg', 'priyanka_93 - Copy (2).jpg', 'priyanka_93 - Copy.jpg', 'priyanka_93.jpg', 'priyanka_94 - Copy (2).jpg', 'priyanka_94 - Copy.jpg', 'priyanka_94.jpg', 'priyanka_95 - Copy (2).jpg', 'priyanka_95 - Copy.jpg', 'priyanka_95.jpg', 'priyanka_96 - Copy (2).jpg', 'priyanka_96 - Copy.jpg', 'priyanka_96.jpg', 'priyanka_97 - Copy (2).jpg', 'priyanka_97 - Copy.jpg', 'priyanka_97.jpg', 'priyanka_98 - Copy (2).jpg', 'priyanka_98 - Copy.jpg', 'priyanka_98.jpg', 'priyanka_99 - Copy (2).jpg', 'priyanka_99 - Copy.jpg', 'priyanka_99.jpg', 'sanjyoti_10 - Copy (2).jpg', 'sanjyoti_10 - Copy.jpg', 'sanjyoti_10.jpg', 'sanjyoti_100 - Copy (2).jpg', 'sanjyoti_100 - Copy.jpg', 'sanjyoti_100.jpg', 'sanjyoti_11 - Copy (2).jpg', 'sanjyoti_11 - Copy.jpg', 'sanjyoti_11.jpg', 'sanjyoti_12 - Copy (2).jpg', 'sanjyoti_12 - Copy.jpg', 'sanjyoti_12.jpg', 'sanjyoti_13 - Copy (2).jpg', 'sanjyoti_13 - Copy.jpg', 'sanjyoti_13.jpg', 'sanjyoti_14 - Copy (2).jpg', 'sanjyoti_14 - Copy.jpg', 'sanjyoti_14.jpg', 'sanjyoti_15 - Copy (2).jpg', 'sanjyoti_15 - Copy.jpg', 'sanjyoti_15.jpg', 'sanjyoti_16 - Copy (2).jpg', 'sanjyoti_16 - Copy.jpg', 'sanjyoti_16.jpg', 'sanjyoti_17 - Copy (2).jpg', 'sanjyoti_17 - Copy.jpg', 'sanjyoti_17.jpg', 'sanjyoti_18 - Copy (2).jpg', 'sanjyoti_18 - Copy.jpg', 'sanjyoti_18.jpg', 'sanjyoti_19 - Copy (2).jpg', 'sanjyoti_19 - Copy.jpg', 'sanjyoti_19.jpg', 'sanjyoti_2 - Copy (2).jpg', 'sanjyoti_2 - Copy.jpg', 'sanjyoti_2.jpg', 'sanjyoti_20 - Copy (2).jpg', 'sanjyoti_20 - Copy.jpg', 'sanjyoti_20.jpg', 'sanjyoti_21 - Copy (2).jpg', 'sanjyoti_21 - Copy.jpg', 'sanjyoti_21.jpg', 'sanjyoti_22 - Copy (2).jpg', 'sanjyoti_22 - Copy.jpg', 'sanjyoti_22.jpg', 'sanjyoti_24 - Copy (2).jpg', 'sanjyoti_24 - Copy.jpg', 'sanjyoti_24.jpg', 'sanjyoti_25 - Copy (2).jpg', 'sanjyoti_25 - Copy.jpg', 'sanjyoti_25.jpg', 'sanjyoti_26 - Copy (2).jpg', 'sanjyoti_26 - Copy.jpg', 'sanjyoti_26.jpg', 'sanjyoti_27 - Copy (2).jpg', 'sanjyoti_27 - Copy.jpg', 'sanjyoti_27.jpg', 'sanjyoti_28 - Copy (2).jpg', 'sanjyoti_28 - Copy.jpg', 'sanjyoti_28.jpg', 'sanjyoti_29 - Copy (2).jpg', 'sanjyoti_29 - Copy.jpg', 'sanjyoti_29.jpg', 'sanjyoti_3 - Copy (2).jpg', 'sanjyoti_3 - Copy.jpg', 'sanjyoti_3.jpg', 'sanjyoti_30 - Copy (2).jpg', 'sanjyoti_30 - Copy.jpg', 'sanjyoti_30.jpg', 'sanjyoti_31 - Copy (2).jpg', 'sanjyoti_31 - Copy.jpg', 'sanjyoti_31.jpg', 'sanjyoti_32 - Copy (2).jpg', 'sanjyoti_32 - Copy.jpg', 'sanjyoti_32.jpg', 'sanjyoti_33 - Copy (2).jpg', 'sanjyoti_33 - Copy.jpg', 'sanjyoti_33.jpg', 'sanjyoti_34 - Copy (2).jpg', 'sanjyoti_34 - Copy.jpg', 'sanjyoti_34.jpg', 'sanjyoti_35 - Copy (2).jpg', 'sanjyoti_35 - Copy.jpg', 'sanjyoti_35.jpg', 'sanjyoti_36 - Copy (2).jpg', 'sanjyoti_36 - Copy.jpg', 'sanjyoti_36.jpg', 'sanjyoti_37 - Copy (2).jpg', 'sanjyoti_37 - Copy.jpg', 'sanjyoti_37.jpg', 'sanjyoti_38 - Copy (2).jpg', 'sanjyoti_38 - Copy.jpg', 'sanjyoti_38.jpg', 'sanjyoti_39 - Copy (2).jpg', 'sanjyoti_39 - Copy.jpg', 'sanjyoti_39.jpg', 'sanjyoti_4 - Copy (2).jpg', 'sanjyoti_4 - Copy.jpg', 'sanjyoti_4.jpg', 'sanjyoti_40 - Copy (2).jpg', 'sanjyoti_40 - Copy.jpg', 'sanjyoti_40.jpg', 'sanjyoti_41 - Copy (2).jpg', 'sanjyoti_41 - Copy.jpg', 'sanjyoti_41.jpg', 'sanjyoti_43 - Copy (2).jpg', 'sanjyoti_43 - Copy.jpg', 'sanjyoti_43.jpg', 'sanjyoti_44 - Copy (2).jpg', 'sanjyoti_44 - Copy.jpg', 'sanjyoti_44.jpg', 'sanjyoti_45 - Copy (2).jpg', 'sanjyoti_45 - Copy.jpg', 'sanjyoti_45.jpg', 'sanjyoti_46 - Copy (2).jpg', 'sanjyoti_46 - Copy.jpg', 'sanjyoti_46.jpg', 'sanjyoti_47 - Copy (2).jpg', 'sanjyoti_47 - Copy.jpg', 'sanjyoti_47.jpg', 'sanjyoti_48 - Copy (2).jpg', 'sanjyoti_48 - Copy.jpg', 'sanjyoti_48.jpg', 'sanjyoti_49 - Copy (2).jpg', 'sanjyoti_49 - Copy.jpg', 'sanjyoti_49.jpg', 'sanjyoti_5 - Copy (2).jpg', 'sanjyoti_5 - Copy.jpg', 'sanjyoti_5.jpg', 'sanjyoti_50 - Copy (2).jpg', 'sanjyoti_50 - Copy.jpg', 'sanjyoti_50.jpg', 'sanjyoti_51 - Copy (2).jpg', 'sanjyoti_51 - Copy.jpg', 'sanjyoti_51.jpg', 'sanjyoti_52 - Copy (2).jpg', 'sanjyoti_52 - Copy.jpg', 'sanjyoti_52.jpg', 'sanjyoti_53 - Copy (2).jpg', 'sanjyoti_53 - Copy.jpg', 'sanjyoti_53.jpg', 'sanjyoti_54 - Copy (2).jpg', 'sanjyoti_54 - Copy.jpg', 'sanjyoti_54.jpg', 'sanjyoti_56 - Copy (2).jpg', 'sanjyoti_56 - Copy.jpg', 'sanjyoti_56.jpg', 'sanjyoti_57 - Copy (2).jpg', 'sanjyoti_57 - Copy.jpg', 'sanjyoti_57.jpg', 'sanjyoti_58 - Copy (2).jpg', 'sanjyoti_58 - Copy.jpg', 'sanjyoti_58.jpg', 'sanjyoti_59 - Copy (2).jpg', 'sanjyoti_59 - Copy.jpg', 'sanjyoti_59.jpg', 'sanjyoti_6 - Copy (2).jpg', 'sanjyoti_6 - Copy.jpg', 'sanjyoti_6.jpg', 'sanjyoti_60 - Copy (2).jpg', 'sanjyoti_60 - Copy.jpg', 'sanjyoti_60.jpg', 'sanjyoti_61 - Copy (2).jpg', 'sanjyoti_61 - Copy.jpg', 'sanjyoti_61.jpg', 'sanjyoti_62 - Copy (2).jpg', 'sanjyoti_62 - Copy.jpg', 'sanjyoti_62.jpg', 'sanjyoti_63 - Copy (2).jpg', 'sanjyoti_63 - Copy.jpg', 'sanjyoti_63.jpg', 'sanjyoti_64 - Copy (2).jpg', 'sanjyoti_64 - Copy.jpg', 'sanjyoti_64.jpg', 'sanjyoti_65 - Copy (2).jpg', 'sanjyoti_65 - Copy.jpg', 'sanjyoti_65.jpg', 'sanjyoti_66 - Copy (2).jpg', 'sanjyoti_66 - Copy.jpg', 'sanjyoti_66.jpg', 'sanjyoti_67 - Copy (2).jpg', 'sanjyoti_67 - Copy.jpg', 'sanjyoti_67.jpg', 'sanjyoti_68 - Copy (2).jpg', 'sanjyoti_68 - Copy.jpg', 'sanjyoti_68.jpg', 'sanjyoti_69 - Copy (2).jpg', 'sanjyoti_69 - Copy.jpg', 'sanjyoti_69.jpg', 'sanjyoti_7 - Copy (2).jpg', 'sanjyoti_7 - Copy.jpg', 'sanjyoti_7.jpg', 'sanjyoti_70 - Copy (2).jpg', 'sanjyoti_70 - Copy.jpg', 'sanjyoti_70.jpg', 'sanjyoti_71 - Copy (2).jpg', 'sanjyoti_71 - Copy.jpg', 'sanjyoti_71.jpg', 'sanjyoti_72 - Copy (2).jpg', 'sanjyoti_72 - Copy.jpg', 'sanjyoti_72.jpg', 'sanjyoti_73 - Copy (2).jpg', 'sanjyoti_73 - Copy.jpg', 'sanjyoti_73.jpg', 'sanjyoti_74 - Copy (2).jpg', 'sanjyoti_74 - Copy.jpg', 'sanjyoti_74.jpg', 'sanjyoti_75 - Copy (2).jpg', 'sanjyoti_75 - Copy.jpg', 'sanjyoti_75.jpg', 'sanjyoti_76 - Copy (2).jpg', 'sanjyoti_76 - Copy.jpg', 'sanjyoti_76.jpg', 'sanjyoti_77 - Copy (2).jpg', 'sanjyoti_77 - Copy.jpg', 'sanjyoti_77.jpg', 'sanjyoti_78 - Copy (2).jpg', 'sanjyoti_78 - Copy.jpg', 'sanjyoti_78.jpg', 'sanjyoti_79 - Copy (2).jpg', 'sanjyoti_79 - Copy.jpg', 'sanjyoti_79.jpg', 'sanjyoti_8 - Copy (2).jpg', 'sanjyoti_8 - Copy.jpg', 'sanjyoti_8.jpg', 'sanjyoti_80 - Copy (2).jpg', 'sanjyoti_80 - Copy.jpg', 'sanjyoti_80.jpg', 'sanjyoti_81 - Copy (2).jpg', 'sanjyoti_81 - Copy.jpg', 'sanjyoti_81.jpg', 'sanjyoti_82 - Copy (2).jpg', 'sanjyoti_82 - Copy.jpg', 'sanjyoti_82.jpg', 'sanjyoti_83 - Copy (2).jpg', 'sanjyoti_83 - Copy.jpg', 'sanjyoti_83.jpg', 'sanjyoti_84 - Copy (2).jpg', 'sanjyoti_84 - Copy.jpg', 'sanjyoti_84.jpg', 'sanjyoti_85 - Copy (2).jpg', 'sanjyoti_85 - Copy.jpg', 'sanjyoti_85.jpg', 'sanjyoti_86 - Copy (2).jpg', 'sanjyoti_86 - Copy.jpg', 'sanjyoti_86.jpg', 'sanjyoti_87 - Copy (2).jpg', 'sanjyoti_87 - Copy.jpg', 'sanjyoti_87.jpg', 'sanjyoti_88 - Copy (2).jpg', 'sanjyoti_88 - Copy.jpg', 'sanjyoti_88.jpg', 'sanjyoti_89 - Copy (2).jpg', 'sanjyoti_89 - Copy.jpg', 'sanjyoti_89.jpg', 'sanjyoti_9 - Copy (2).jpg', 'sanjyoti_9 - Copy.jpg', 'sanjyoti_9.jpg', 'sanjyoti_90 - Copy (2).jpg', 'sanjyoti_90 - Copy.jpg', 'sanjyoti_90.jpg', 'sanjyoti_91 - Copy (2).jpg', 'sanjyoti_91 - Copy.jpg', 'sanjyoti_91.jpg', 'sanjyoti_92 - Copy (2).jpg', 'sanjyoti_92 - Copy.jpg', 'sanjyoti_92.jpg', 'sanjyoti_93 - Copy (2).jpg', 'sanjyoti_93 - Copy.jpg', 'sanjyoti_93.jpg', 'sanjyoti_94 - Copy (2).jpg', 'sanjyoti_94 - Copy.jpg', 'sanjyoti_94.jpg', 'sanjyoti_95 - Copy (2).jpg', 'sanjyoti_95 - Copy.jpg', 'sanjyoti_95.jpg', 'sanjyoti_96 - Copy (2).jpg', 'sanjyoti_96 - Copy.jpg', 'sanjyoti_96.jpg', 'sanjyoti_97 - Copy (2).jpg', 'sanjyoti_97 - Copy.jpg', 'sanjyoti_97.jpg', 'sanjyoti_98 - Copy (2).jpg', 'sanjyoti_98 - Copy.jpg', 'sanjyoti_98.jpg', 'sanjyoti_99 - Copy (2).jpg', 'sanjyoti_99 - Copy.jpg', 'sanjyoti_99.jpg', 'subhasish_1 - Copy (2).jpg', 'subhasish_1 - Copy.jpg', 'subhasish_1.jpg', 'subhasish_10 - Copy (2).jpg', 'subhasish_10 - Copy.jpg', 'subhasish_10.jpg', 'subhasish_100 - Copy (2).jpg', 'subhasish_100 - Copy.jpg', 'subhasish_100.jpg', 'subhasish_11 - Copy (2).jpg', 'subhasish_11 - Copy.jpg', 'subhasish_11.jpg', 'subhasish_12 - Copy (2).jpg', 'subhasish_12 - Copy.jpg', 'subhasish_12.jpg', 'subhasish_13 - Copy (2).jpg', 'subhasish_13 - Copy.jpg', 'subhasish_13.jpg', 'subhasish_14 - Copy (2).jpg', 'subhasish_14 - Copy.jpg', 'subhasish_14.jpg', 'subhasish_15 - Copy (2).jpg', 'subhasish_15 - Copy.jpg', 'subhasish_15.jpg', 'subhasish_17 - Copy (2).jpg', 'subhasish_17 - Copy.jpg', 'subhasish_17.jpg', 'subhasish_2 - Copy (2).jpg', 'subhasish_2 - Copy.jpg', 'subhasish_2.jpg', 'subhasish_20 - Copy (2).jpg', 'subhasish_20 - Copy.jpg', 'subhasish_20.jpg', 'subhasish_21 - Copy (2).jpg', 'subhasish_21 - Copy.jpg', 'subhasish_21.jpg', 'subhasish_22 - Copy (2).jpg', 'subhasish_22 - Copy.jpg', 'subhasish_22.jpg', 'subhasish_23 - Copy (2).jpg', 'subhasish_23 - Copy.jpg', 'subhasish_23.jpg', 'subhasish_24 - Copy (2).jpg', 'subhasish_24 - Copy.jpg', 'subhasish_24.jpg', 'subhasish_25 - Copy (2).jpg', 'subhasish_25 - Copy.jpg', 'subhasish_25.jpg', 'subhasish_26 - Copy (2).jpg', 'subhasish_26 - Copy.jpg', 'subhasish_26.jpg', 'subhasish_27 - Copy (2).jpg', 'subhasish_27 - Copy.jpg', 'subhasish_27.jpg', 'subhasish_28 - Copy (2).jpg', 'subhasish_28 - Copy.jpg', 'subhasish_28.jpg', 'subhasish_29 - Copy (2).jpg', 'subhasish_29 - Copy.jpg', 'subhasish_29.jpg', 'subhasish_3 - Copy (2).jpg', 'subhasish_3 - Copy.jpg', 'subhasish_3.jpg', 'subhasish_30 - Copy (2).jpg', 'subhasish_30 - Copy.jpg', 'subhasish_30.jpg', 'subhasish_31 - Copy (2).jpg', 'subhasish_31 - Copy.jpg', 'subhasish_31.jpg', 'subhasish_32 - Copy (2).jpg', 'subhasish_32 - Copy.jpg', 'subhasish_32.jpg', 'subhasish_33 - Copy (2).jpg', 'subhasish_33 - Copy.jpg', 'subhasish_33.jpg', 'subhasish_34 - Copy (2).jpg', 'subhasish_34 - Copy.jpg', 'subhasish_34.jpg', 'subhasish_35 - Copy (2).jpg', 'subhasish_35 - Copy.jpg', 'subhasish_35.jpg', 'subhasish_37 - Copy (2).jpg', 'subhasish_37 - Copy.jpg', 'subhasish_37.jpg', 'subhasish_38 - Copy (2).jpg', 'subhasish_38 - Copy.jpg', 'subhasish_38.jpg', 'subhasish_39 - Copy (2).jpg', 'subhasish_39 - Copy.jpg', 'subhasish_39.jpg', 'subhasish_4 - Copy (2).jpg', 'subhasish_4 - Copy.jpg', 'subhasish_4.jpg', 'subhasish_40 - Copy (2).jpg', 'subhasish_40 - Copy.jpg', 'subhasish_40.jpg', 'subhasish_42 - Copy (2).jpg', 'subhasish_42 - Copy.jpg', 'subhasish_42.jpg', 'subhasish_43 - Copy (2).jpg', 'subhasish_43 - Copy.jpg', 'subhasish_43.jpg', 'subhasish_44 - Copy (2).jpg', 'subhasish_44 - Copy.jpg', 'subhasish_44.jpg', 'subhasish_45 - Copy (2).jpg', 'subhasish_45 - Copy.jpg', 'subhasish_45.jpg', 'subhasish_46 - Copy (2).jpg', 'subhasish_46 - Copy.jpg', 'subhasish_46.jpg', 'subhasish_47 - Copy (2).jpg', 'subhasish_47 - Copy.jpg', 'subhasish_47.jpg', 'subhasish_48 - Copy (2).jpg', 'subhasish_48 - Copy.jpg', 'subhasish_48.jpg', 'subhasish_49 - Copy (2).jpg', 'subhasish_49 - Copy.jpg', 'subhasish_49.jpg', 'subhasish_5 - Copy (2).jpg', 'subhasish_5 - Copy.jpg', 'subhasish_5.jpg', 'subhasish_50 - Copy (2).jpg', 'subhasish_50 - Copy.jpg', 'subhasish_50.jpg', 'subhasish_51 - Copy (2).jpg', 'subhasish_51 - Copy.jpg', 'subhasish_51.jpg', 'subhasish_52 - Copy (2).jpg', 'subhasish_52 - Copy.jpg', 'subhasish_52.jpg', 'subhasish_53 - Copy (2).jpg', 'subhasish_53 - Copy.jpg', 'subhasish_53.jpg', 'subhasish_54 - Copy (2).jpg', 'subhasish_54 - Copy.jpg', 'subhasish_54.jpg', 'subhasish_55 - Copy (2).jpg', 'subhasish_55 - Copy.jpg', 'subhasish_55.jpg', 'subhasish_56 - Copy (2).jpg', 'subhasish_56 - Copy.jpg', 'subhasish_56.jpg', 'subhasish_57 - Copy (2).jpg', 'subhasish_57 - Copy.jpg', 'subhasish_57.jpg', 'subhasish_58 - Copy (2).jpg', 'subhasish_58 - Copy.jpg', 'subhasish_58.jpg', 'subhasish_59 - Copy (2).jpg', 'subhasish_59 - Copy.jpg', 'subhasish_59.jpg', 'subhasish_6 - Copy (2).jpg', 'subhasish_6 - Copy.jpg', 'subhasish_6.jpg', 'subhasish_60 - Copy (2).jpg', 'subhasish_60 - Copy.jpg', 'subhasish_60.jpg', 'subhasish_61 - Copy (2).jpg', 'subhasish_61 - Copy.jpg', 'subhasish_61.jpg', 'subhasish_62 - Copy (2).jpg', 'subhasish_62 - Copy.jpg', 'subhasish_62.jpg', 'subhasish_63 - Copy (2).jpg', 'subhasish_63 - Copy.jpg', 'subhasish_63.jpg', 'subhasish_64 - Copy (2).jpg', 'subhasish_64 - Copy.jpg', 'subhasish_64.jpg', 'subhasish_65 - Copy (2).jpg', 'subhasish_65 - Copy.jpg', 'subhasish_65.jpg', 'subhasish_66 - Copy (2).jpg', 'subhasish_66 - Copy.jpg', 'subhasish_66.jpg', 'subhasish_67 - Copy (2).jpg', 'subhasish_67 - Copy.jpg', 'subhasish_67.jpg', 'subhasish_68 - Copy (2).jpg', 'subhasish_68 - Copy.jpg', 'subhasish_68.jpg', 'subhasish_69 - Copy (2).jpg', 'subhasish_69 - Copy.jpg', 'subhasish_69.jpg', 'subhasish_7 - Copy (2).jpg', 'subhasish_7 - Copy.jpg', 'subhasish_7.jpg', 'subhasish_70 - Copy (2).jpg', 'subhasish_70 - Copy.jpg', 'subhasish_70.jpg', 'subhasish_71 - Copy (2).jpg', 'subhasish_71 - Copy.jpg', 'subhasish_71.jpg', 'subhasish_72 - Copy (2).jpg', 'subhasish_72 - Copy.jpg', 'subhasish_72.jpg', 'subhasish_73 - Copy (2).jpg', 'subhasish_73 - Copy.jpg', 'subhasish_73.jpg', 'subhasish_74 - Copy (2).jpg', 'subhasish_74 - Copy.jpg', 'subhasish_74.jpg', 'subhasish_75 - Copy (2).jpg', 'subhasish_75 - Copy.jpg', 'subhasish_75.jpg', 'subhasish_76 - Copy (2).jpg', 'subhasish_76 - Copy.jpg', 'subhasish_76.jpg', 'subhasish_77 - Copy (2).jpg', 'subhasish_77 - Copy.jpg', 'subhasish_77.jpg', 'subhasish_78 - Copy (2).jpg', 'subhasish_78 - Copy.jpg', 'subhasish_78.jpg', 'subhasish_8 - Copy (2).jpg', 'subhasish_8 - Copy.jpg', 'subhasish_8.jpg', 'subhasish_80 - Copy (2).jpg', 'subhasish_80 - Copy.jpg', 'subhasish_80.jpg', 'subhasish_81 - Copy (2).jpg', 'subhasish_81 - Copy.jpg', 'subhasish_81.jpg', 'subhasish_82 - Copy (2).jpg', 'subhasish_82 - Copy.jpg', 'subhasish_82.jpg', 'subhasish_83 - Copy (2).jpg', 'subhasish_83 - Copy.jpg', 'subhasish_83.jpg', 'subhasish_84 - Copy (2).jpg', 'subhasish_84 - Copy.jpg', 'subhasish_84.jpg', 'subhasish_85 - Copy (2).jpg', 'subhasish_85 - Copy.jpg', 'subhasish_85.jpg', 'subhasish_86 - Copy (2).jpg', 'subhasish_86 - Copy.jpg', 'subhasish_86.jpg', 'subhasish_87 - Copy (2).jpg', 'subhasish_87 - Copy.jpg', 'subhasish_87.jpg', 'subhasish_88 - Copy (2).jpg', 'subhasish_88 - Copy.jpg', 'subhasish_88.jpg', 'subhasish_89 - Copy (2).jpg', 'subhasish_89 - Copy.jpg', 'subhasish_89.jpg', 'subhasish_9 - Copy (2).jpg', 'subhasish_9 - Copy.jpg', 'subhasish_9.jpg', 'subhasish_90 - Copy (2).jpg', 'subhasish_90 - Copy.jpg', 'subhasish_90.jpg', 'subhasish_91 - Copy (2).jpg', 'subhasish_91 - Copy.jpg', 'subhasish_91.jpg', 'subhasish_92 - Copy (2).jpg', 'subhasish_92 - Copy.jpg', 'subhasish_92.jpg', 'subhasish_93 - Copy (2).jpg', 'subhasish_93 - Copy.jpg', 'subhasish_93.jpg', 'subhasish_94 - Copy (2).jpg', 'subhasish_94 - Copy.jpg', 'subhasish_94.jpg', 'subhasish_95 - Copy (2).jpg', 'subhasish_95 - Copy.jpg', 'subhasish_95.jpg', 'subhasish_96 - Copy (2).jpg', 'subhasish_96 - Copy.jpg', 'subhasish_96.jpg', 'subhasish_97 - Copy (2).jpg', 'subhasish_97 - Copy.jpg', 'subhasish_97.jpg', 'subhasish_98 - Copy (2).jpg', 'subhasish_98 - Copy.jpg', 'subhasish_98.jpg', 'subhasish_99 - Copy (2).jpg', 'subhasish_99 - Copy.jpg', 'subhasish_99.jpg']\n"
     ]
    }
   ],
   "source": [
    "print(os.listdir(img_dir))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f2a130ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\USER\\\\Desktop\\\\AI AND ML\\\\project\\\\AI_ML PROJECT\\\\images'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_dir"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "75eee2aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "images = np.array(images)\n",
    "labels = np.array(labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3dea4730",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'mona', 'priyanka', 'sanjyoti', 'subhasish'}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "58065cd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c301ba48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mona : 294\n",
      "subhasish : 282\n",
      "sanjyoti : 288\n",
      "priyanka : 255\n"
     ]
    }
   ],
   "source": [
    "for i in set(labels):\n",
    "    t = sum(labels==i)\n",
    "    print(f\"{i} : {t}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0eaffb38",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1119, 100, 100)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "images.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "5ce3b29d",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(os.path.join(data_dir,'images.p'),'wb') as f:\n",
    "    pickle.dump(images,f)\n",
    "\n",
    "with open(os.path.join(data_dir,'labels.p'),'wb') as f:\n",
    "    pickle.dump(labels,f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d17e5f4e",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
