# databalloon
---
#### *`Πρόταση για το 1ο Μαθητικό Συνέδριο "Ερευνητικές Διαδρομές στον Πολιτισμό και στις Επιστήμες" ΔΔΕ Ανατολικής Αττικής`*
---
# Κατασκευή και Προγραμματισμός Αιωρούμενου Μετεωρολογικού Σταθμού. Λήψη, Επεξεργασία και Οπτικοποίηση Δεδομένων.
---
### Περίληψη:
Η εργασία αφορά την κατασκευή ενός μετεωρολογικού σταθμού ο οποίος αιωρείται με τη βοήθεια ενός μετεωρολογικού μπαλονιού. Σκοπός μας ήταν να δημιουργήσουμε έναν μετεωρολογικό σταθμό, ώστε να παρακολουθούμε σε πραγματικό χρόνο διάφορα περιβαλλοντικά δεδομένα, όπως θερμοκρασία, υγρασία, βαρομετρική πίεση, υψόμετρο, περιστροφική κίνηση. Στο εργαστήριο πληροφορικής αξιοποιήσαμε τους μικροελεγκτές micro:bit για να συνθέσουμε κυκλώματα με αντίστοιχους αισθητήρες και να πειραματιστούμε με αυτά. Αρχικά ξεκινήσαμε την υλοποίηση προγραμματίζοντας μέσω του περιβάλλοντος https://makecode.microbit.org σε γλώσσα με πλακίδια. Μέσω της radio επικοινωνίας,  ένα micro:bit “αποστολέας”, εκπέμπει τα δεδομένα από τους αισθητήρες σε άλλο κοντινό micro:bit “παραλήπτη”. Αυτό με τη σειρά του στέλνει τα δεδομένα στη θύρα USB υπολογιστή όπου προβάλλονται σε πραγματικό χρόνο σε οθόνη, ενώ παράλληλα μπορούν να αποθηκευθούν σε μορφή csv για περαιτέρω επεξεργασία με ένα υπολογιστικό φύλλο. Στην πορεία, κατά την σύνθεση του μετεωρολογικού σταθμού, τοποθετήσαμε όλα τα εξαρτήματα σε κατάλληλο κουτί το οποίο ζυγίστηκε, ενώ υπολογίσαμε το απαραίτητο μέγεθος του μπαλονιού, καθώς και την ποσότητα σε αέριο ήλιο, ώστε να μπορέσει να ανυψωθεί όλη η διάταξη. Τέλος η κατασκευή αγκυρώθηκε εξωτερικά στη στέγη του εργαστηρίου πληροφορικής, ώστε να αιωρείται αρκετά ψηλά. Από τους υπολογιστές της αίθουσας συλλέξαμε τα δεδομένα για να εξάγουμε μέγιστες, ελάχιστες και μέσες τιμές, ενώ μπορέσαμε να δημιουργήσουμε χρήσιμα γραφήματα. Η εργασία μας είναι διαθέσιμη και στο αποθετήριό μας https://github.com/robpeta/databalloon.


## Radio Επικοινωνία μικροελεγκτών micro:bit. Μέτρηση Εμβέλειας

Πρόγραμμα [Sender] αποστολής δεδομένων αισθητήρα "ένταση φωτεινότητας" [light level] από ένα micro:bit σε ένα άλλο. Οι τιμές του αισθητήρα αποστέλλονται μαζί με τo όνομα της μεταβλητής "x". 
Sender--->Receiver


[![Sender](./Sender_snapshot.png)](https://makecode.microbit.org/_JLX3AwTbxdhs/)


Πρόγραμμα [Receiver] λήψης δεδομένων αισθητήρα "ένταση φωτεινότητας" [light level] από ένα micro:bit, προκειμένου να γίνει η μέτρηση εμβέλειας. Οι τιμές του αισθητήρα λαμβάνονται μαζί με το όνομα της μεταβλητής , στη μορφή [name=value].  Η εντολή [if] χρησιμοποιείται για να ελέγξει εάν το όνομα της ληφθείσας μεταβλητής είναι "x", [name="x"]. Τοτε, σε αυτή την περίπτωση γνωρίζουμε πως τα δεδομένα αφορούν τον αισθητήρα "ένταση φωτεινότητας" [light level]

[![Receiver](./Receiver_snapshot.png)](https://makecode.microbit.org/_A6E4iCC1kLoV/)


