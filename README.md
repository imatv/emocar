Emocar
======

Mind-controlled Arduino Uno rover using an Emotiv EPOC neuroheadset.  
Original concept by Alvin Vuong, Daniel Kho, Ethan Harte, and Nikita Sokolnikov.  
CalHacks 2014.

**Description**  

By reading raw EEG data from an 16-channel Emotiv EPOC neuroheadset, we were able to isolate and understand what part of one's brain dealt with certain thoughts. With some research and data visualization, we came to see the various lobes of the brain in action. Then by isolating and analyzing the EEG data from the parietal lobe of the brain, we were able to use machine learning methods in order to train a threshold for the brain activity in order to produce a "Go" command. This command is consequently sent through serial port to the Arduino on-board the rover, which then activates the motors and wheels to propel the rover forward.

In summary, we made a crude brain-computer interface that can now allow one to control basic motor functions with his/her mind. Many applications can arise from brain-computer interfaces. The physically disabled and paralyzed can take advantage of this technology to help with their lives. Not to mention, telekinesis is just plain awesome.

(A notable obstacle that we had to overcome in this project was that the data from the EPOC headset was encrypted to begin with. We had to send the data through an open-source toolkit called Emokit that figured out the decryption. Then we tried to use open-source brain-computer interfaces to help us process the data, but ran into compatibility and installation issues. This was solved by hard-coding our own crude BCI, and we were ecstatic to make it work as well as it did.)
