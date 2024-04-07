# databalloon
---
#### *`Πρόταση για το 1ο Μαθητικό Συνέδριο "Ερευνητικές Διαδρομές στον Πολιτισμό και στις Επιστήμες" ΔΔΕ Ανατολικής Αττικής`*
---
# Κατασκευή και Προγραμματισμός Αιωρούμενου Μετεωρολογικού Σταθμού. Λήψη, Επεξεργασία και Οπτικοποίηση Δεδομένων.
---
### Περίληψη
Η εργασία αφορά την κατασκευή ενός μετεωρολογικού σταθμού ο οποίος αιωρείται με τη βοήθεια ενός μετεωρολογικού μπαλονιού. Σκοπός μας ήταν να δημιουργήσουμε έναν μετεωρολογικό σταθμό, ώστε να παρακολουθούμε σε πραγματικό χρόνο διάφορα περιβαλλοντικά δεδομένα, όπως θερμοκρασία, υγρασία, βαρομετρική πίεση, υψόμετρο, περιστροφική κίνηση. Στο εργαστήριο πληροφορικής αξιοποιήσαμε τους μικροελεγκτές micro:bit για να συνθέσουμε κυκλώματα με αντίστοιχους αισθητήρες και να πειραματιστούμε με αυτά. Αρχικά ξεκινήσαμε την υλοποίηση προγραμματίζοντας μέσω του περιβάλλοντος https://makecode.microbit.org σε γλώσσα με πλακίδια. Μέσω της radio επικοινωνίας,  ένα micro:bit “αποστολέας”, εκπέμπει τα δεδομένα από τους αισθητήρες σε άλλο κοντινό micro:bit “παραλήπτη”. Αυτό με τη σειρά του στέλνει τα δεδομένα στη θύρα USB υπολογιστή, όπου προβάλλονται σε πραγματικό χρόνο σε οθόνη, ενώ παράλληλα μπορούν να αποθηκευθούν σε μορφή csv για περαιτέρω επεξεργασία με ένα υπολογιστικό φύλλο. Στην πορεία, κατά την σύνθεση του μετεωρολογικού σταθμού, τοποθετήσαμε όλα τα εξαρτήματα σε κατάλληλο κουτί το οποίο ζυγίστηκε, ενώ υπολογίσαμε το απαραίτητο μέγεθος του μπαλονιού, καθώς και την ποσότητα σε αέριο ήλιο, ώστε να μπορέσει να ανυψωθεί όλη η διάταξη. Τέλος η κατασκευή αγκυρώθηκε εξωτερικά στη στέγη του εργαστηρίου πληροφορικής, ώστε να αιωρείται αρκετά ψηλά. Από τους υπολογιστές της αίθουσας συλλέξαμε τα δεδομένα για να εξάγουμε μέγιστες, ελάχιστες και μέσες τιμές, ενώ μπορέσαμε να δημιουργήσουμε χρήσιμα γραφήματα. Η εργασία μας είναι διαθέσιμη και στο αποθετήριό μας https://github.com/robpeta/databalloon.

### Η Ιδέα
Η ιδέα προήλθε από τα μετεωρολογικά μπαλόνια (ειδικά μπαλόνια υψηλού υψομέτρου) που απελευθερώνονται για να φτάσουν στη στρατόσφαιρα, μεταφέροντας όργανα ικανά να μετρήσουν και να στείλουν πίσω στη γη χρήσιμες πληροφορίες όπως, ατμοσφαιρική πίεση, υγρασία, θερμοκρασία, ταχύτητα ανέμου. Τα μπαλόνια αυτά χρησιμοποιούνται για τη διάγνωση των τρεχουσών συνθηκών που επικρατούν στις περιοχές από όπου εκτοξεύονται. Θελήσαμε να δημιουργήσουμε στο Σχολείο μας έναν μετεωρολογικό σταθμό, ο οποίος όμως θα αιωρείται αγκυρωμένος στη σκεπή του Εργαστηρίου Πληροφορικής και θα παρέχει περίπου αντίστοιχες περιβαλλοντικές πληροφορίες με εκείνες ενός κανονικού μετεωρολογικού μπαλονιού.

### Υλικά & Μέθοδος
Η όλη σύνθεση αποτελείται από τρία βασικά μέρη: 
1. το μετεωρολογικό μπαλόνι
2. τη διάταξη ενός μικροελεγκτή με τους αισθητήρες, όπου θα προσαρτηθεί στο μπαλόνι (κύκλωμα Εικόνας 2) :
   1. 1 micro:bit για την αποστολή των δεδομένων (αποστολέας)
   2. 1 micro:bit edge connector, για την πρόσβαση στις επαφές του micro:bit
   3. 1 Αισθητήρα θερμοκρασίας και υγρασίας (dht11)
   4. 1 Αισθητήρα βαρομετρικής πίεσης και θερμοκρασίας (BMP280)
   5. 1 Αντίσταση 10 ΚΩ
   6. 1 breadboard για τη σύνθεση των κυκλωμάτων
   7. αντίστοιχα καλώδια
   8. 1 μπαταριοθήκη με καλώδιο JST-PH για τροφοδοσία
   9. 2 μπαταρίες ΑΑ
3. τους μικροελεγκτές για τη λήψη των δεδομένων:
   1. 1 micro:bit για ενδιάμεση λήψη & αναμετάδοση δεδομένων (αναμεταδότης)
   2. 1 micro:bit για την τελική λήψη δεδομένων (παραλήπτης)

#### Το Μετεωρολογικό Μπαλόνι
Το μετεωρολογικό μπαλόνι που επιλέχθηκε ζυγίζει 200g και μπορεί να σηκώσει επιπλέον βάρος 200g. Το αέριο που χρησιμοποιήθηκε είναι ήλιο, διότι θεωρείται πολύ πιο ασφαλές από το υδρογόνο το οποίο σε κατάλληλες συνθήκες εκρηγνύεται. Για το συγκεκριμένο μπαλόνι χρειάστηκε ήλιο όγκου $`0.5m^3`$ με πίεση 55mbar από μπουκάλα των 8lt (Εικόνα 1).

**Εικόνα 1**. Το μετεωρολογικό μπαλόνι έξω από το εργαστήριο πληροφορικής

![the balloon](./Weather_Balloon.png)

#### Η Διάταξη micro:bit με τους Αισθητήρες
Το micro:bit είναι ένας μικροελεγκτής αρκετά μικρού μεγέθους, με ενσωματωμένους αισθητήρες και δυνατότητα να επικοινωνεί ασύρματα με άλλα micro:bit, ενώ παράλληλα προγραμματίζεται σε περιβάλλον με πλακίδια, καθιστώντας το έτσι ιδανικό για ένα τέτοιο έργο. Το επίσημο προγραμματιστικό περιβάλλον είναι το https://makecode.microbit.org

**Εικόνα 2**: Σχέδιο συνδεσμολογίας micro:bit με τους αισθητήρες

![microbit and sensors](microbit_and_2sensors.png)

**Δοκιμή 1: Εύρεση εμβέλειας επικοινωνίας μεταξύ δύο micro:bit.**

Αρχικά το πρώτο πράγμα που θελήσαμε να δοκιμάσουμε ήταν η μέγιστη απόσταση από την οποία μπορούν να επικοινωνούν 2 micro:bit μεταξύ τους. Για το σκοπό αυτό προγραμματίσαμε το ένα ως “αποστολέα” (Εικόνα 3), στέλνοντας την τιμή του αισθητήρα φωτεινότητας στο άλλο, “παραλήπτη” (Εικόνα 4), στη μορφή [x = τιμή αισθητήρα]. Όταν ο “παραλήπτης” λάβει μήνυμα με όνομα μεταβλητής “x”, εμφανίζεται στην οθόνη του ένα εικονίδιο για 500ms, δηλώνοντας την επιτυχή λήψη του σήματος. Με αυτόν τον τρόπο  βρήκαμε πως η μέγιστη απόσταση επικοινωνίας μεταξύ τους είναι περίπου 18m.

**Εικόνα 3**: Πρόγραμμα micro:bit Δοκιμής 1, σε ρόλο “αποστολέα” δεδομένων.

[![Sender](./Sender_snapshot.png)](https://makecode.microbit.org/_JLX3AwTbxdhs/)

**Εικόνα 4**: Πρόγραμμα micro:bit Δοκιμής 1, σε ρόλο “παραλήπτη” δεδομένων.

[![Receiver](./Receiver_snapshot.png)](https://makecode.microbit.org/_A6E4iCC1kLoV/)

**Δοκιμή 2: Μετάδοση σήματος μέσα από τη μεταλλική στέγη.**

Με τη διάταξη των δύο micro:bit “αποστολέας” - “παραλήπτης”, δοκιμάσαμε επίσης κατά πόσο η μεταλλική στέγη του εργαστηρίου Πληροφορικής, επιτρέπει την επικοινωνία μεταξύ των δύο μικροελεγκτών. Τοποθετώντας το ένα έξω και πάνω στη στέγη και έχοντας το άλλο μέσα στο εργαστήριο, διαπιστώσαμε πως η επικοινωνία είναι εφικτή μόνο πλησιάζοντας το δεύτερο micro:bit κοντά στο ταβάνι. Αυτό σήμαινε πως όταν θα χρησιμοποιούσαμε το μετεωρολογικό μπαλόνι, τα δεδομένα από τους αισθητήρες δεν θα μπορούσαν να φτάσουν στους υπολογιστές μέσα στο εργαστήριο Πληροφορικής.

Η λύση στο πρόβλημα αυτό δόθηκε χρησιμοποιώντας ένα επιπλέον micro:bit “αναμεταδότη” το οποίο βρίσκεται σε κοινή θέα με τον “αποστολέα” και τον “παραλήπτη” (Εικόνα 5). Ο ρόλος του “αναμεταδότη” είναι: 
για όσο βρίσκεται στο κοινό κανάλι 1 (radio group 1) με τον “αποστολέα”, να αποθηκεύει τις τιμές των αισθητήρων που λαμβάνει, σε αντίστοιχες μεταβλητές. 
στη συνέχεια μεταβαίνοντας  στο κανάλι 5 (radio group 5), να στέλνει τις τιμές αυτές στον “παραλήπτη”, μέσα στο εργαστήριο πληροφορικής.

**Εικόνα 5**: Σχεδιάγραμμα αποστολής και λήψης δεδομένων.

![radio communication](radio_communication.png)

#### Παραγωγή και αποστολή δεδομένων
Για την εξαγωγή των δεδομένων από τους αισθητήρες dht11 (θερμοκρασίας και υγρασίας) και BMP280 (βαρομετρικής πίεσης και θερμοκρασίας) και την αποστολή αυτών σε άλλο micro:bit χρησιμοποιήθηκε το πρόγραμμα της Εικόνας 7. Οι εντολές για τη διαχείριση των δύο αισθητήρων, μπορούν να φορτωθούν στο προγραμματιστικό περιβάλλον μέσα από την ιστοσελίδα makecode.microbit.org, επιλέγοντας από την περιοχή των εντολών  και στη συνέχεια κάνοντας αναζήτηση “dht11” και “bmp280” αντίστοιχα. Το παρακάτω πρόγραμμα αποτελείται από 2 κύρια blocks:
1. [on start]: αρχικά θέτουμε το radio group σε 1, μεταξύ “αποστολέα” και “παραλήπτη” και την ισχύ μετάδοσης στο μέγιστο (7). Οι επόμενες δύο εντολές, γαλάζιου χρώματος έχουν να κάνουν με την ενεργοποίηση και την διευθυνσιοδότηση του αισθητήρα BMP280, όπως δίνεται από τον κατασκευαστή (χρησιμοποιεί πρωτόκολλο επικοινωνίας i2c).
2. [forever]: οι εντολές χρώματος πορτοκαλί, αναφέρονται στον αισθητήρα dht11. Εδώ με τις εντολές radio send value τα δεδομένα “στέλνονται” κάθε 1 δευτερόλεπτο στη μορφή [“όνομα_μεταβλητής” = τιμή_μεταβλητής]. Τέλος, ο ενσωματωμένος αισθητήρας accelerometer, σχετίζεται με τις περιστροφές (rotation (o) roll & rotation (o) pitch) (Εικόνα 6) και αξιοποιείται για να ληφθεί η κατάσταση αιώρησης του micro:bit “αποστολέα”.

**Εικόνα 6**: Περιγραφή των περιστροφών roll και pitch που αντιλαμβάνεται ο αισθητήρας


