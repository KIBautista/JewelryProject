#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is a user-input based "Yes" and "No" styled quiz used to determine the material of a costume jewelry bead or gemstone. This is used to differentiate between the materials: glass, semiprecious, CZ, or acrylic / plastic. 

#This begins with the first question 

question = input (" \n Welcome! \n \n To determine a bead, stone, or cab material, \n type in answers to the following questions: \n \n Is it cold to touch? \n Yes or No?")
if question == "yes" or " yes" :
question2 = input (" \n Does it make a high pitched sound when tapped? \n Yes or No?")
if question2 == "yes" or " yes":
question3 = input (" \n Is it transluscent? \n Yes or No?")
if question3 == "yes" or " yes":
question5 = input (" \n Does it shine like a rainbow? \n Yes or No?")
if question5 == "yes" or "yes":

#This is the end of the first branch, which outputs the material CZ. 
# First appearance of CZ output. 

outcome2 = input (" \n This may be CZ. \n CZ will always be in a setting where the back is open, in order for light to shine through. \n Check references for CZ. \n If the stone is in a closed-back setting, \n this may be glass.")
if question5 == "no" or " no":
  
#This is the end of the first branch, which outputs the material Glass. 
outcome4 = input (" \n This may be glass. \n Compare to glass references. \n Glass will be cool to touch, and make a sharp sound when tapped. \n Stones will usually be in a closed-back setting. \n There is no seam or gate on glass stones or beads.")

#This is the end of the first branch, which outputs the material Semiprecious. 
if question3 == "no" or " no":
outcome1 = input (" \n This may be semiprecious. \n Check references for semiprecious stones. \n If you do not think this is semiprecious, re-assess answers, get a second opinion, and try again.")
if question5 == "yes" or "yes":
  
# Second appearance of CZ output. 
outcome2 = input (" \n This may be CZ. \n CZ will always be in a setting where the back is open, in order for light to shine through. \n Check references for CZ. \n If the stone is in a closed-back setting, \n this may be glass.")
if question5 == "no" or " no":
  
  
outcome4 = input (" \n This may be glass. \n Compare to glass references. \n Glass will be cool to touch, and make a sharp sound when tapped. \n Stones will usually be in a closed-back setting. \n There is no seam or gate on glass stones or beads.")
if question5 == "yes" or " yes":
  
# Third appearance of CZ output. 
outcome2 = input (" \n This may be CZ. \n CZ will always be in a setting where the back is open, in order for light to shine through. \n Check references for CZ. \n If the stone is in a closed")
if question2 == "no" or " no":
  

question6 = input (" \n Does it have a seam or gate? \n *Tip-A gate is a small hole on the side of the bead or stone. \n Yes or No?")
if question6 == "yes" or " yes":
outcome3 = input ("\n This may be acrylic. \n Acrylic is dull in shine, and will have \n a gate or seam on the edge. \n If the component is warm \n and dull when tapped, but does not \n contain a seam or gate, \n then it may be Resin. \n For more information on 'Resin' enter 'more'")
if outcome3 == "more" or " more":
more1 = input (" \n Resin is still a plastic-based material, \n but the quality is better than acrylic \n because the process is different. \n Resin stones or beads are individually injected \n into a mold, which is why there is no gate or seam. \n Acrylic is mass produced, multiple components at once \n created into a sheet which is then broken apart, hence the appearance of a gate or seam.")
if question2 == "yes" or " yes":
outcome4 = input (" \n This may be glass. \n Compare to glass references. \n Glass will be cool to touch, and make a sharp sound when tapped. \n Stones will usually be in a closed-back setting. \n There is no seam or gate on glass stones or beads.")
question3 = input (" \n Is it transluscent? \n Yes or No?")
if question3 == "yes" or " yes":
question5 = input (" \n Does it shine like a rainbow? \n Yes or No?")
if question5 == "yes" or " yes":
  
# Forth appearance of the CZ output.
outcome2 = input (" \n This may be CZ. \n CZ will always be in a setting where the back is open, in order for light to shine through. \n Check references for CZ. \n If the stone is in a closed-back setting, \n this may be glass.")
if question5 == "no" or " no":
outcome4 = input (" \n This may be glass. \n Compare to glass references. \n Glass will be cool to touch, and make a sharp sound when tapped. \n Stones will usually be in a closed-back setting. \n There is no seam or gate on glass stones or beads.")
if question3 == "no" or " no":
outcome1 = input (" \n This may be semiprecious. \n Check references for semiprecious stones. \n If you do not think this is semiprecious, re-assess answers, get a second opinion, and try again.")
if question == "no" or " no":
question4 = input (" \n Is the bead warm to touch? Yes or No?")
if question4 == "yes" or " yes":
question6 = input (" \n Does it have a seam or gate? *Tip-A gate is a small hole on the side of the bead or stone. Yes or No?")
if question6 == "yes" or " yes":
outcome3 = input ("\n This may be acrylic. \n Acrylic is dull in shine, and will have \n a gate or seam on the edge. \n If the component is warm \n and dull when tapped, but does not \n contain a seam or gate, \n then it may be Resin. \n For more information on 'Resin' enter 'more.'")
if outcome3 == "more" or " more":
more1 = input (" \n Resin is still a plastic-based material, \n but the quality is better than acrylic \n because the process is different. \n Resin stones or beads are individually injected \n into a mold, which is why there is no gate or seam. \n Acrylic is mass produced, multiple components at once \n created into a sheet which is then broken apart, hence the appearance of a gate or seam.")
