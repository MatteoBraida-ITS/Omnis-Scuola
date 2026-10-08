# PRD Template

# PRD di Omnis Scuola · Team [nome del team]

<aside>
💡

**Come usare questo template**

Duplica questa pagina e compilala con il tuo team. Dove trovi del testo in _corsivo_, sostituiscilo con il vostro. I callout 💡 sono consigli per te: cancellali prima della consegna da questo markdown.

Il documento ha due parti. Nella prima scrivi **cosa** fa Omnis Scuola, nella seconda **come** lo costruirai. Tienile separate. Chi legge la prima parte deve capire tutto senza sapere cos'è Spring Boot.

Un buon PRD sta fra le 15 e le 25 pagine. Se ne scrivi di più, probabilmente stai descrivendo invece di decidere.

</aside>

---

## Informazioni sul documento

|              |               |
| ------------ | ------------- |
| **Prodotto** | Omnis Scuola  |
| **Team**     | Braida Matteo |
| **Autori**   | Matteo Braida |
| **Versione** | _1.0_         |
| **Data**     | _25/09/2026_  |
| **Stato**    | Bozza         |

### Storico delle versioni

| Versione | Data       | Autore        | Cosa è cambiato e perché |
| -------- | ---------- | ------------- | ------------------------ |
| 1.0      | 25/09/2026 | Matteo Braida | Prima stesura            |
|          |            |               |                          |

<aside>
💡

Il PRD cambierà durante l'anno. Ogni modifica va registrata qui, con la sua ragione. Un PRD che dice una cosa mentre il codice ne fa un'altra è peggio di nessun PRD.

</aside>

---

# Prima parte · Il cosa

## Scopo e perimetro

### Perché esiste Omni Scuola

**Dal lato business.** _Oggi il materiale didattico, verifiche e voti viaggiano su canali diversi come Email, chiavette USB, fogli di carta e registri separati. Omni Scuola si occupa di tenere tutto questo in unico posto con un’interfaccia semplice e facile da navigare._

**Dal lato tecnico.** _Omni scuola è una applicazione web accessibile da PC e telefono che copre la creazione e gestione di nuovi utenti (Docenti e studenti) creazione di verifiche, assegnamento dei voti e pubblicazione di materiale. Ogni utente può interfacciarsi a questa applicazione solo nel modo in cui il suo ruolo gli consente._

### Cosa è incluso

- Creazione account docenti e studenti tramite invio di un link dove l’utente potrà creare le proprie credenziali e conseguente mail di verifica.
- Creazione delle classi, assegnazione degli studenti e dei docenti con le loro materie.
- Pubblicazione di materiale didattico (file e link) da parte del docente, visibile alle sue classi.
- Creazione di verifiche online con domande a risposta multipla e a risposta aperta.
- Assegnazione dei voti, sia alle verifiche online sia a prove svolte fuori da Omni Scuola (orali, scritti su carta)
- Consultazione dei propri voti da parte dello studente, divisi per materia e con la media
- Una vista d'insieme per il Direttore su classi, docenti, studenti e voti

---

### Cosa non è incluso

- Omnis scuola NON gestisce i ritardi assenze e orari delle lezioni.
- Omnis scuola NON gestisce le comunicazioni con le famiglie e non prevede l’accesso per i genitori.
- Omnis scuola NON ha chat e forum.
- Omnis scuola NON è un’app da installare ma è una applicazione visitabile solo da browser.
- Omnis scuola gestisce solo una scuola alla volta NON una rete di istituti.

<aside>
💡

La lista di cosa **non** è incluso è la più preziosa del documento. Ogni riga qui ti evita una settimana di discussioni più avanti.

</aside>

---

## Stakeholder

| Stakeholder                 | Cosa fa                                                               | Cosa gli interessa                                                                              | Come lo coinvolgete                                                            |
| --------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Direttore                   | Controlla l’attivita generale di docenti e studenti.                  | Avere un quadro completo degli studenti e delle attività svolte dai docenti.                    | Revisione del PRD, prova della sua area riservata prima del collaudo.          |
| Docenti                     | Crea e corregge verifiche, assegna voti e carica materiale didattico. | Risparmiare tempo nella correzione; avere uno strumento semplice anche per chi è poco digitale. | Prova della creazione della verifica, assegnamento voti e upload di materiale. |
| Studenti                    | Consultano il materiale, svolgono verifiche e visualizzano i voti.    | Materiale didattico sempre accessibile, sezione verifiche solida e accessibile.                 | Intervista sui requisiti impliciti e collaudo.                                 |
| Docente del corso           | Valida il PRD                                                         | Scelte motivate, requisiti verificabili e coerenza tra le parti.                                | Presentazione e domande                                                        |
| Collaudatori del primo anno | Usano Omnis Scuola come utenti reali                                  | Che l’app sia chiara e facile da utilizzare                                                     | _Intervista, collaudo_                                                         |
| _Altri?_                    |                                                                       |                                                                                                 |                                                                                |

<aside>
💡

Gli stakeholder non sono solo gli utenti. Sono anche chi approva, chi paga, chi manterrà il sistema. Chiediti chi resterebbe deluso se Omnis Scuola non funzionasse.

</aside>

---

## Destinatari e contesto d'uso

### La scuola che avete immaginato

_Descrivi la scuola per cui progettate. Che tipo di istituto è, dove si trova, come si organizza la giornata. Questi dati tornano nella stima del carico, quindi scegli numeri che poi userai davvero._

|                    | Valore                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| Numero di studenti | 920                                                                                                 |
| Numero di docenti  | 75                                                                                                  |
| Numero di classi   | 40 (Con all’interno una media di 23 studenti)                                                       |
| Orario scolastico  | _es. 8:00 – 14:00, dal lunedì al venerdì_                                                           |
| Connettività       | _es. Wi-Fi scolastico condiviso, rete cablata nei laboratori e in caso rete mobile degli studenti._ |

### Gli archetipi

Arricchisci gli archetipi della traccia.

| ID      | Archetipo | Contesto d'uso                                                                                                                                                                                             | Competenze digitali                                                                                                                                                                                 | Dispositivo principale                                                                                     | Frequenza d'uso                                                                                                           |
| ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ARC-001 | Direttore | Principalmente nel suo ufficio durante le ore di lezione. Si occupa della configurazione iniziale a settembre, monitora la situazione durante l'anno e controlla i tabelloni dei voti a fine quadrimestre. | Discrete. Usa ogni giorno la mail, Excel e il vecchio software della segreteria. Non ha tempo da perdere dietro a interfacce complicate o procedure lunghe.                                         | PC desktop dell'ufficio                                                                                    | Altissima a settembre (per creare le classi e mandare gli inviti), poi controlli settimanali e picco a fine quadrimestre. |
| ARC-002 | Docente   | Carica i materiali e prepara i compiti da casa o nei momenti buchi in sala docenti. Usa l'app in aula per registrare al volo i voti.                                                                       | Molto variabili. Ci sono professori giovani smanettoni e docenti più anziani che fanno fatica con la tecnologia, cercano i passaggi più veloci e hanno il terrore di cancellare i dati per sbaglio. | Portatile personale a casa, PC della sala professori o computer della cattedra per gli inserimenti rapidi. | Due o tre volte a settimana, con picchi notevoli nei periodi dei compiti in classe e degli scrutini.                      |
| ARC-003 | Studente  | Svolge i compiti in classe nel laboratorio di informatica o usando i PC della scuola. Controlla i voti e scarica le dispense durante le pause o a casa.                                                    | Nativo digitale sullo smartphone, ma a volte in difficoltà con il computer (gestione di cartelle e file). Vuole un'interfaccia immediata e senza spiegazioni, tipo social network.                  | PC del laboratorio o notebook scolastico per i compiti; smartphone personale per guardare i voti.          | Praticamente quotidiana per controllare i materiali; occasionale per lo svolgimento delle verifiche.                      |
|         |

<aside>
💡

I collaudatori veri sono i ragazzi del primo anno. Usano lo smartphone in corridoio o il PC in laboratorio? La risposta cambia l'interfaccia, i requisiti di usabilità e perfino il dimensionamento.

</aside>

---

## Panoramica e casi d'uso

### In poche righe

Omnis Scuola nasce per facilitare la gestione del materiale didattico, delle verifiche e dei voti in un'unica piattaforma. L'obiettivo principale è eliminare il disordine generato dallo scambio di email, chiavette USB smarrite o fogli di carta volanti: con questa applicazione, docenti e studenti hanno tutto a portata di click, aggiornato in tempo reale.

Il Direttore si occupa di configurare le classi e invitare docenti e studenti, mantenendo una visione globale sull'andamento dell'istituto. I docenti possono caricare dispense per le proprie classi, strutturare quiz e compiti da svolgere online, e registrare i voti (compresi quelli delle interrogazioni orali o dei compiti scritti). Gli studenti hanno un'area riservata in cui scaricare i materiali, svolgere i test assegnati e monitorare i propri voti con il calcolo automatico della media per materia.

### User story principali

**Direttore (DIR)**

- **DIR-T01:** Come Direttore, voglio poter caricare direttamente un elenco fornito dalla segreteria per invitare gli studenti, evitando di dover inserire gli account uno alla volta a inizio anno.
- **DIR-T02:** Come Direttore, voglio controllare lo stato degli inviti (se non sono arrivati o se sono scaduti) e poterli reinviare con un click, per assicurarmi che tutti i ragazzi riescano ad accedere prima dell'inizio delle lezioni.
- **DIR-T03:** Come Direttore, voglio spostare uno studente da una sezione all'altra senza che questo perda tutti i voti che ha già preso nel quadrimestre.

**Docenti (DOC)**

- **DOC-T01:** Come docente, voglio salvare i materiali didattici come bozza prima di pubblicarli, così da poterli ricontrollare con calma senza farli vedere subito alle classi.
- **DOC-T02:** Come docente, voglio poter annullare una domanda scritta male o sbagliata anche dopo che il compito è finito, facendo ricalcolare in automatico i voti a tutta la classe senza penalizzare nessuno.
- **DOC-T03:** Come docente, voglio mettere sulla piattaforma anche i voti delle prove classiche (come le interrogazioni orali o i temi scritti su carta), per avere tutti i voti di una materia in un solo registro.

**Studenti (STU)**

- **STU-T01:** Come studente, voglio attivare il mio account cliccando sul link ricevuto via mail e scegliere una mia password sicura al primo accesso.
- **STU-T02:** Come studente, voglio vedere un avviso chiaro sul sito non appena un professore pubblica un nuovo voto o carica dei nuovi file da studiare.
- **STU-T03:** Come studente, voglio poter rivedere il mio compito corretto sul sito, controllando gli errori che ho fatto e leggendo i commenti lasciati dal professore.

---

### SCENARI D'USO E FLUSSI UTENTE

### DIR-01/02 · Creazione degli account degli studenti

**Flusso dei passaggi (User flow)**

1. Il Direttore fa il login ed entra nella sezione dedicata agli studenti.
2. Clicca su "Importa elenco" e seleziona il file fornito dalla segreteria (che contiene nome, cognome, email e classe).
3. L'applicazione mostra una schermata di anteprima, dividendo i nomi scritti bene da quelli che contengono errori.
4. Il Direttore conferma: il sistema crea gli utenti in stato "da attivare" e spedisce in automatico le mail con i link.
5. Il Direttore può controllare lo stato di ogni mail: inviata, accettata, scaduta o non consegnata.

**Scenario principale**
A inizio settembre il Direttore riceve dalla segreteria il file dei nuovi iscritti. Lo carica sul sito, controlla che sia tutto a posto nell'anteprima e preme conferma. In pochi minuti tutti gli studenti ricevono l'invito sulla propria posta elettronica. Dopo una settimana, il Direttore vede dal suo pannello che quasi tutti hanno attivato l'account e contatta i pochi rimasti indietro per sollecitarli.

**Scenari alternativi**

- **Il file contiene righe scritte male (es. manca la mail o ci sono duplicati):** il sistema segnala visivamente i nomi errati e li scarta, permettendo comunque di caricare tutti quelli corretti. Il Direttore sistema i dati mancanti e ricarica solo le righe che erano state scartate.
- **Un invito è scaduto prima dell'utilizzo:** il Direttore clicca su reinvia. Questa azione genera un nuovo link e disattiva immediatamente quello vecchio, che non funzionerà più.
- **Uno studente è già registrato nel sistema:** l'applicazione lo segnala nella schermata di riepilogo e non crea un doppione.

### DOC-02 · Gestione e creazione dei compiti in classe

**Flusso dei passaggi (User flow)**

1. Il professore crea una nuova verifica selezionando la classe e la propria materia.
2. Inserisce le domande a risposta multipla (indicando i punti e qual è quella giusta) e i quesiti a risposta aperta.
3. Sceglie il giorno, l'ora esatta di inizio e la durata in minuti del compito.
4. La verifica compare nella pagina degli studenti solo all'orario spaccato stabilito.
5. Quando i ragazzi consegnano, il sistema corregge da solo le risposte multiple, mentre il prof corregge a mano quelle aperte.
6. Il professore conferma e pubblica i voti sul registro.

**Scenario principale**
Il professore prepara un quiz di 10 domande (8 a crocette e 2 aperte), programmato per martedì alle 9:00 con una durata di 50 minuti. Non appena scatta l'ora, il test si sblocca sui PC degli alunni. Al termine del tempo, le domande chiuse sono già calcolate dal sistema; la sera stessa il professore corregge da casa le due domande aperte rimaste e clicca per pubblicare i voti finali.

**Scenari alternativi**

- **Una domanda conteneva un errore e il compito è già finito:** il professore clicca su "Annulla domanda". Il sistema cancella quel quesito dal test e ricalcola all'istante i voti di tutti i ragazzi escludendo il punteggio di quella domanda.
- **Il professore prova a cambiare le domande dopo l'inizio del compito:** il sistema blocca la modifica. L'unica azione concessa a compito aperto o chiuso è l'annullamento di una domanda.
- **Il professore si dimentica di segnare la risposta giusta in una crocetta:** quando prova a salvare, il programma blocca la pubblicazione e mostra un avviso visivo che indica quale domanda va completata.

### STU-02 · Svolgimento di un compito online

**Flusso dei passaggi (User flow)**

1. Lo studente si siede alla sua postazione nel laboratorio di informatica e fa il login.
2. Va nella sezione verifiche e seleziona il compito del giorno, leggendo quanto tempo ha a disposizione.
3. Clicca su "Avvia" e il timer del server inizia il conto alla rovescia.
4. Risponde alle domande: il sistema salva ogni singola risposta nel database un secondo dopo averla inserita.
5. Il ragazzo clicca su consegna, oppure il compito si chiude da solo non appena il tempo finisce.
6. La schermata mostra un messaggio di conferma del salvataggio.

**Scenario principale**
Martedì alle 9:00 gli studenti aprono la pagina del test di informatica in laboratorio. Rispondono alle domande una alla volta, terminano il compito dopo 45 minuti, cliccano su consegna e vedono la conferma che il testo è stato inviato correttamente.

**Scenari alternativi**

- **La connessione Wi-Fi della scuola ha un calo temporaneo:** le risposte date fino a quel secondo sono al sicuro nel database. Quando la linea internet ritorna, la pagina si aggiorna mostrando le risposte già inserite e il tempo reale rimanente, calcolato dal server.
- **Il tempo a disposizione finisce prima della consegna:** il sistema blocca la scrittura e invia in automatico il compito salvando le risposte inserite fino a quel momento.
- **Lo studente prova a fare il furbo e apre il test in due schede del browser insieme:** il programma mantiene attiva solo l'ultima pagina aperta e scollega immediatamente la prima, mostrando un messaggio di errore.
- **Lo studente prova ad entrare nel compito prima dell'ora o a test scaduto:** il pulsante per iniziare rimane grigio e non cliccabile.

## Requisiti funzionali

### Le user story della traccia

### Tabella di corrispondenza dei requisiti

| Area    | Significato                        | Codici dei Requisiti Associati                                                                           |
| ------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **INV** | Inviti e attivazione degli account | FR-INV-01 (Blocco email) · FR-INV-02 (Scadenza link)                                                     |
| **CLA** | Classi e studenti                  | FR-CLA-01 (Cambio classe alunno)                                                                         |
| **VER** | Verifiche e quiz                   | FR-VER-01 (Modifica quiz aperto) · FR-VER-02 (Scheda singola) · FR-VER-03 (Salvataggio se cade internet) |
| **VOT** | Registro dei voti                  | FR-VOT-01 (Scala 1-10) · FR-VOT-02 (Calcolo media semplice) · FR-VOT-03 (Registro delle modifiche)       |
| **MAT** | Materiale e dispense               | FR-MAT-01 (Limiti di peso sui file)                                                                      |
| **NOT** | Avvisi interni                     | FR-NOT-01 (Pallini di notifica sul sito)                                                                 |

### Dettagli delle Storie Utente e Criteri di Accettazione

| ID         | Funzionalità                    | Controlli e Comportamento del Sistema                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Note                             |
| ---------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **DIR-01** | Creare account docente          | • Il Direttore scrive i dati e la mail del docente: il sistema crea l'utente in stato "in attesa" e gli manda un link di invito via mail.<br>• Se la mail inserita esiste già nel database, il sistema blocca tutto e mostra un messaggio di errore chiaro.<br>• Il link scade dopo 7 giorni. Il professore deve inventarsi una password valida entro questo limite per attivare l'account.                                                                                                                                                                                                                                                                                                                 | FR-INV-01, FR-INV-02.            |
| **DIR-02** | Creare account studente         | • Il Direttore carica l'elenco fornito dalla segreteria: il sistema salva solo i nomi scritti bene. Le righe con errori o dati mancanti vengono scartate e mostrate in un riepilogo finale con spiegato il motivo.<br>• Se uno studente è già registrato non viene duplicato, ma viene segnalato nel riepilogo.<br>• Se un invito scade o va perso, il Direttore può cliccare su "Reinvia": questo disattiva il vecchio link e ne spedisce uno nuovo di zecca.                                                                                                                                                                                                                                              | FR-INV-01, FR-INV-02.            |
| **DIR-03** | Creare e gestire le classi      | • Il sistema impedisce di creare due classi con lo stesso nome nello stesso anno scolastico.<br>• Quando si associa un prof a una classe per una determinata materia, il prof vedrà e potrà agire solo su quella specifica materia.<br>• Se un alunno cambia sezione, il trasferimento mantiene intatti tutti i suoi vecchi voti e le sue medie. Dal momento dello spostamento, il ragazzo vede solo i compiti e i file della nuova classe.                                                                                                                                                                                                                                                                 | FR-CLA-01                        |
| **DIR-04** | Schermata generale della scuola | • La pagina riassuntiva del Direttore mostra per ogni classe il totale degli iscritti, l'elenco dei prof e la media attuale per materia.<br>• Se in una materia non ci sono ancora valutazioni, il sistema mostra la scritta "Nessun voto" invece di uno zero numerico.<br>• Questa schermata è in sola lettura: il Direttore non può modificare i voti da questa pagina.                                                                                                                                                                                                                                                                                                                                   |                                  |
| **DOC-01** | Caricare dispense e file        | • I file salvati come "Bozza" rimangono nascosti agli studenti finché il prof non clicca per pubblicarli.<br>• Il sistema controlla il peso del file (massimo 20 MB) e il tipo di documento durante il caricamento. Se non vanno bene mostra un errore, ma lascia intatti gli altri testi già scritti nel modulo.<br>• Un file già pubblicato può essere rimesso in "Bozza" in qualsiasi momento, facendolo sparire all'istante dalla vista dei ragazzi.                                                                                                                                                                                                                                                    | FR-MAT-01.                       |
| **DOC-02** | Preparare i quiz online         | • Non si possono cambiare le domande o i punti di un compito dopo che è iniziato. L'unica cosa permessa è annullare una domanda scritta male.<br>• Annullare una domanda la elimina dal conteggio del compito e ricalcola all'istante i voti totali di tutti gli studenti che lo hanno svolto.<br>• Il sistema blocca la pubblicazione dei quiz se ci sono domande a risposta multipla dove il prof si è dimenticato di segnare qual è la risposta corretta.                                                                                                                                                                                                                                                | FR-VER-01.                       |
| **DOC-03** | Inserire i voti nel registro    | • Il sistema rifiuta qualsiasi voto fuori dalla scala consentita (accetta solo da 1 a 10 con scatti di 0,5, rifiutando scritte o segni come "+").<br>• Il registro permette al prof di inserire a mano i voti delle interrogazioni orali o dei compiti tradizionali scritti su carta, chiedendo il nome del ragazzo, la data e il tipo di prova.<br>• Se un professore cambia o cancella un voto già salvato, il sistema memorizza di nascosto chi lo ha fatto, il giorno, l'ora e il valore che c'era prima.                                                                                                                                                                                               | FR-VOT-01, FR-VOT-02, FR-VOT-03. |
| **STU-01** | Guardare il materiale didattico | • Lo studente vede solo le dispense e i link delle materie della sua classe, ordinati partendo dai file caricati più di recente.<br>• Se un ragazzo clicca su un link di invito scaduto per registrarsi, il sistema blocca la procedura e mostra un avviso che dice di chiedere un nuovo invio alla segreteria.                                                                                                                                                                                                                                                                                                                                                                                             |                                  |
| **STU-02** | Svolgere una verifica online    | • Il sistema non fa entrare nel quiz se lo studente ci prova prima dell'orario di inizio o dopo l'orario di chiusura fissato dal prof.<br>• Ogni risposta viene salvata nel database un secondo dopo essere stata cliccata. Se salta internet, quando torna la linea il ragazzo ritrova le sue risposte e il tempo rimanente corretto, perché il timer lo calcola il server e non il PC dell'aula.<br>• Quando il tempo scade, il compito si chiude e si consegna da solo inviando quello che è stato risposto fino a quel momento.<br>• Si può aprire il test su una sola scheda alla volta: se lo studente prova ad aprirlo in un'altra pagina o sul telefono, la sessione precedente si scollega subito. | FR-VER-02, FR-VER-03             |
| **STU-03** | Controllare la propria pagella  | • I voti non ancora pubblicati o confermati dal professore rimangono invisibili nell'area dello studente.<br>• Nella sua pagina, il ragazzo vede l'elenco delle materie con la media aritmetica aggiornata. Se in una materia non ha voti, compare la scritta "Nessun voto".<br>• Cliccando su un voto di un compito online pubblicato, l'interfaccia mostra: le risposte date, quelle giuste e le correzioni scritte dal professore.                                                                                                                                                                                                                                                                       | FR-VOT-02, FR-NOT-01.            |

<aside>
💡

Gli acceptance criteria della traccia sono il minimo. Puoi aggiungerne, non toglierne. Scrivi quelli nuovi nello stesso formato _Dato che / Quando / Allora_.

</aside>

### Le decisioni prese sui punti aperti della traccia

Durante lo studio dei requisiti sono emersi diversi aspetti che la traccia lasciava in sospeso o che andavano chiariti prima di iniziare a scrivere il codice delle tabelle e le funzioni del programma. Di seguito sono elencate le scelte che ho fatto, pensate per tenere il codice il più semplice possibile e per facilitare l'uso dell'applicazione.

> **FR-VOT-01 · Scala dei voti** (collegato a DOC-03)
> Nel registro si possono inserire solo voti numerici da 1 a 10, con scatti di 0,5 (ad esempio 5.5, 6, 6.5). Non è permesso inserire simboli come "+" o "−", né scritte a testo libero.
> _Motivazione:_ Gestire i voti solo come numeri normali rende facile il calcolo automatico della media nel codice ed evita fraintendimenti tra i professori (ad esempio, mettersi d'accordo su quanto valga un "6 meno meno" in cifre).

> **FR-CLA-01 · Trasferimento di uno studente** (collegato a DIR-03, DIR-T03)
> Il Direttore può spostare un alunno in un'altra classe in qualunque momento. I voti presi fino a quel giorno rimangono nel profilo dello studente, legati alla materia e al professore che li ha messi, continuando a fare media. Dal momento del cambio classe, lo studente vedrà solo i file e i compiti della nuova sezione.
> _Motivazione:_ Un cambio di sezione per motivi personali o scolastici non deve far perdere il lavoro già fatto dal ragazzo. I voti sono legati al percorso dello studente e non alla classe in cui si trova.

> **FR-VER-01 · Modifica di una verifica dopo l'apertura** (collegato a DOC-02, DOC-T02)
> Quando una verifica comincia, il docente non può più cambiare il testo o l'ordine delle domande. L'unica cosa che può fare è annullare una domanda (ad esempio se si accorge di un errore). Se lo fa, il sistema toglie quella domanda dal totale del compito e ricalcola subito i voti di tutti gli studenti.
> _Motivazione:_ Cambiare le domande mentre i ragazzi stanno rispondendo creerebbe solo confusione e ingiustizie nel test. L'annullamento è il modo più pulito per correggere una svista del prof senza penalizzare nessuno.

> **FR-VER-02 · Sessione unica** (collegato a STU-02)
> Ogni studente può fare la verifica attiva su una sola pagina web per volta. Se prova ad aprire lo stesso compito in un'altra scheda del browser o da un altro dispositivo (ad esempio dal telefono), la pagina precedente si chiude subito e mostra un messaggio di avviso.
> _Motivazione:_ Questa scelta serve a evitare che risposte diverse inviate nello stesso momento si sovrascrivano nel database e impedisce che ci siano due timer diversi che scorrono per lo stesso alunno.

> **FR-VER-03 · Gestione della rete durante i test** (collegato a STU-02)
> Il programma salva ogni risposta nel database non appena lo studente la seleziona o la scrive. Il tempo rimanente del test viene calcolato dal server e continua a scorrere anche se internet si disconnette. Quando la linea torna, lo studente riprende esattamente da dove era rimasto con il tempo reale rimasto. Se il tempo scade, il server blocca il compito e salva quello che è stato risposto fino a quel momento.
> _Motivazione:_ In questo modo il ragazzo non perde il lavoro fatto se il Wi-Fi della scuola ha un calo temporaneo, e allo stesso tempo si evita che qualcuno scolleghi apposta il cavo di rete per guadagnare minuti extra.

> **FR-INV-01 · Gestione dei blocchi dell'email** (collegato a DIR-01, DIR-02, DIR-T02)
> Se il servizio esterno che invia le mail (Brevo) ha un problema o non risponde, l'applicazione non si blocca: l'invito viene messo in una lista d'attesa nel database e il sistema riprova a mandarlo da solo ogni 5 minuti. Il Direttore può comunque controllare la lista e cliccare per riprovare l'invio a mano.
> _Motivazione:_ Il guasto momentaneo di un sito esterno non deve bloccare il lavoro del Direttore, che deve sempre poter vedere chi ha ricevuto l'accesso e chi è rimasto fuori.

> **FR-INV-02 · Scadenza dei link di invito** (collegato a DIR-01, DIR-02, STU-T01)
> I link inviati via mail per creare la propria password valgono per 7 giorni e si possono usare una volta sola. Se il Direttore clicca per reinviare l'invito, il vecchio link si disattiva immediatamente e vale solo quello nuovo.
> _Motivazione:_ È una sicurezza di base per evitare che link di registrazione rimangano attivi per sempre se finiscono nelle mani sbagliate, e una settimana basta e avanza per fare il primo accesso.

> **FR-MAT-01 · Limiti sui file allegati** (collegato a DOC-01)
> Si possono caricare i file didattici più comuni (PDF, Word, Excel, Powerpoint e immagini) con un limite di 20 MB per file. In alternativa, il prof può semplicemente incollare un link esterno (ad esempio di Google Drive o di YouTube).
> _Motivazione:_ Questa soluzione copre tutte le esigenze dei docenti senza riempire subito la memoria del server economico che ho scelto, aiutando a tenere i costi del cloud fissi e bassi.

> **FR-VOT-02 · Come viene calcolata la media** (collegato a DOC-03, STU-03, DIR-04)
> La media che si vede nei registri e nelle schermate è una media aritmetica semplice di tutti i voti pubblicati. Non ci sono pesi diversi tra compiti scritti, orali o test online. Se non ci sono voti, compare la scritta "Nessun voto".
> _Motivazione:_ È la soluzione più semplice e veloce da programmare in questa prima versione del software. Gestire medie ponderate o configurazioni diverse per ogni materia richiederebbe una struttura molto più complessa, rimandata a sviluppi futuri.

> **FR-VOT-03 · Registro delle modifiche dei voti** (collegato a DOC-03)
> Il database tiene traccia di qualsiasi modifica o cancellazione fatta sui voti. Per ogni variazione il sistema memorizza chi ha fatto il cambio, il giorno, l'ora esatta e il valore del voto prima della modifica.
> _Motivazione:_ I voti scolastici hanno un valore ufficiale ed è fondamentale, sia per il Direttore che per i professori, poter controllare la cronologia dei cambiamenti in caso di errori di distrazione o contestazioni dei ragazzi.

> **FR-NOT-01 · Logica delle notifiche** (collegato a STU-T02)
> Gli avvisi per i nuovi voti o per i nuovi materiali caricati compaiono solo all'interno dell'applicazione. Lo studente vedrà un pallino di avviso non appena fa il login sul sito. Non vengono spedite mail per queste attività.
> _Motivazione:_ Evita di riempire le caselle di posta degli studenti con messaggi continui e azzera il consumo del piano gratuito del servizio email, che preferisco tenere da conto solo per gli inviti.

---

## Requisiti non funzionali

| ID         | Famiglia      | Requisito                                     | Soglia e condizione                                                                                                                                                                                | Come si verifica                                                                                                                                              | Storie collegate       |
| ---------- | ------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **NFR-01** | Prestazioni   | Tempo di risposta nel picco delle verifiche   | Il caricamento delle domande e l'invio del modulo devono richiedere meno di 2 secondi sotto il carico di una classe intera (circa 30 studenti) che avvia il test nello stesso istante.             | Si prova l'applicazione simulando più accessi contemporanei dai PC del laboratorio a inizio ora.                                                              | STU-02                 |
| **NFR-02** | Prestazioni   | Fluidità nell'uso quotidiano delle bacheche   | Le pagine di consultazione voti e il download dei materiali didattici devono caricarsi in meno di 3 secondi in condizioni di normale attività di rete.                                             | Controllo visivo dei tempi di caricamento delle pagine durante le normali prove di utilizzo del software.                                                     | STU-01, STU-03, DIR-04 |
| **NFR-03** | Sicurezza     | Controllo dei permessi lato server            | Il sistema deve bloccare chiunque provi a forzare gli indirizzi web per fare cose non permesse (es. uno studente che prova a digitare l'indirizzo della pagina di inserimento voti dei prof).      | Si prova a fare l'accesso a pagine riservate usando l'account di un ruolo non autorizzato, controllando che il sistema mostri un errore.                      | DIR-04, DOC-03, STU-03 |
| **NFR-04** | Sicurezza     | Criteri di accesso e blocco tentativi errati  | Le password nel database devono essere criptate (non salvate in chiaro); lunghezza minima di 10 caratteri; blocco temporaneo dell'account per 15 minuti dopo 5 tentativi di login falliti.         | Si controlla nel database che i testi delle password siano illeggibili e si prova a sbagliare il login per 5 volte di fila per vedere se il blocco si attiva. | STU-01, DIR-01, DIR-02 |
| **NFR-05** | Usabilità     | Semplicità dell'interfaccia per utenti comuni | Almeno l'80% degli studenti della classe di test deve completare il quiz senza richiedere spiegazioni; un docente deve poter registrare un voto orale in meno di un minuto al primo tentativo.     | Sessione di test sul campo osservando il comportamento dei compagni e dei prof reali, cronometrando quanto ci mettono a fare le azioni.                       | STU-02, DOC-03         |
| **NFR-06** | Disponibilità | Protezione da perdite di dati e salvataggi    | Nessun voto o risposta già confermata deve andare persa se il server si spegne per un guasto. Il database deve salvarsi in automatico ogni notte, tenendo lo storico per 30 giorni.                | Si spegne forzatamente il server locale durante una simulazione per verificare che i dati non siano persi e si fa una prova di ripristino dal file di backup. | STU-02, DOC-03         |
| **NFR-07** | Ambientale    | Compatibilità con i computer della scuola     | La grafica dell'applicazione deve adattarsi e vedersi bene sui PC del laboratorio con schermi piccoli (da 1366×768 in su) e supportare i browser Chrome, Firefox ed Edge.                          | Si apre l'applicazione direttamente dai computer della scuola e si controlla che tabelle e pulsanti siano allineati e leggibili.                              | STU-02, DOC-01         |
| **NFR-08** | Supporto      | Autonomia nella gestione delle credenziali    | Le procedure di recupero password e la gestione dei link scaduti devono essere risolvibili in autonomia dagli utenti o tramite il pannello del Direttore, senza dover toccare il codice.           | Si fa una prova di smarrimento credenziali durante i test seguendo i passaggi indicati nella guida utente scritta per i prof e i ragazzi.                     | DIR-01, DIR-02, STU-01 |
| **NFR-09** | Interazione   | Feedback immediato e messaggi di errore       | Qualsiasi operazione di salvataggio o errore deve mostrare un avviso visivo chiaro entro un secondo. Le azioni che non si possono annullare (es. cancellare un voto) devono chiedere una conferma. | Si clicca sui pulsanti dell'applicazione e si controlla che compaiano le finestre di avviso e i messaggi di errore corretti.                                  | STU-02, DOC-02, DOC-03 |
| **NFR-10** | Conformità    | Rispetto delle normative sulla privacy (GDPR) | Memorizzazione dei dati su server che si trovano in Europa (Hetzner Germania). I voti devono essere visibili solo all'alunno interessato, ai suoi docenti e al Direttore.                          | Si verifica sul pannello di controllo del cloud la posizione del server e si controlla nel codice che un utente non veda i dati altrui.                       | STU-03, DIR-04         |

---

<aside>
💡

Le famiglie da coprire sono queste. **Prestazioni, disponibilità, scalabilità, sicurezza** e **conformità** vengono dalla lezione sui requisiti funzionali e non funzionali. **Usabilità, ambientali, supporto** e **interazione** vengono dalla lezione sul PRD. Se una famiglia resta vuota, scrivi perché non vi riguarda.

I requisiti trasversali della traccia (HTTPS, paginazione, OpenAPI, errori uniformi, Dev e Prod) sono già obbligatori. Riportali qui con il loro ID.

</aside>

### Requisiti impliciti

Prima di chiudere questa sezione, intervista per dieci minuti un ragazzo del primo anno. La domanda è una sola. _"Cosa daresti per scontato che un'app di questo tipo faccia sempre, o non faccia mai?"_

| Chi avete intervistato | Cosa ha detto                     | Requisito che ne avete ricavato |
| ---------------------- | --------------------------------- | ------------------------------- |
| _nome o iniziali_      | _"Il voto non deve sparire, mai"_ | _NFR-…_                         |
|                        |                                   |                                 |

---

## Assunzioni, vincoli e dipendenze

### Assunzioni

| ID         | Assunzione                                                                                                                        | Cosa succede se si rivela falsa (Impatto e Soluzioni)                                                                                                                                                                          |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ASS-01** | La popolazione scolastica si attesta sui 920 studenti, 75 docenti e 40 classi complessive.                                        | I calcoli fatti nella stima del carico e la scelta della taglia del server VPS andranno rivisti, con il rischio di dover fare un upgrade hardware se i numeri aumentano molto.                                                 |
| **ASS-02** | Il numero massimo di studenti in contemporanea sotto verifica è di 125, vincolato dal numero di PC funzionanti nei laboratori.    | Se la scuola introduce l'uso dei dispositivi personali in classe per i test, il picco delle ore 9:00 aumenterà drasticamente e bisognerà ottimizzare le query per evitare colli di bottiglia.                                  |
| **ASS-03** | Tutti i docenti e gli studenti dispongono di una casella email attiva e regolarmente consultata.                                  | Il sistema di inviti automatici via mail fallirà. Come soluzione di backup, la segreteria dovrà poter generare e stampare un foglio con il link/token di attivazione cartaceo per i ragazzi senza mail.                        |
| **ASS-04** | La segreteria scolastica è in grado di estrarre e fornire i dati dei nuovi iscritti in un formato file .csv o Excel.              | La feature di importazione massiva diventa inutile. Il Direttore sarà costretto a inserire manualmente l'anagrafica di ogni singolo studente, allungando a dismisura i tempi di attivazione iniziale.                          |
| **ASS-05** | L'infrastruttura di rete interna dei laboratori è stabile e ha abbastanza banda per gestire tutte le postazioni connesse insieme. | L'applicazione risulterà lenta o irraggiungibile per colpa della rete locale, anche se il server cloud risponde perfettamente. In questo caso andrà contattato il tecnico informatico dell'istituto per risolvere il problema. |
| **ASS-06** | Gli studenti utilizzeranno la piattaforma da casa (con la propria rete) per controllare i voti e scaricare le dispense.           | Tutto il traffico dati si sposterà esclusivamente nella fascia oraria scolastica (8:00 - 14:00), congestionando le richieste sul server invece di distribuirle durante la giornata.                                            |
|            |

### Vincoli

| ID         | Vincolo                                                                                                                                                                                                                                            | Da dove viene                   |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **VIN-01** | **Requisiti tecnici obbligatori del corso:** Utilizzo di HTTPS, paginazione dei dati nelle liste, documentazione delle API tramite OpenAPI/Swagger, gestione uniforme degli errori e separazione degli ambienti (Local/Dev e Production in Cloud). | Traccia del progetto d'esame    |
| **VIN-02** | **Conformità Privacy e GDPR:** Trattamento rigoroso dei dati personali degli utenti, tenendo conto che la piattaforma ospiterà anche dati sensibili di studenti minorenni.                                                                         | Normativa europea sulla privacy |
| **VIN-03** | **Accessibilità per le PA:** L'interfaccia web deve rispettare le linee guida WCAG 2.1 livello AA, come previsto per i software destinati alla scuola pubblica italiana.                                                                           | Legge Stanca                    |
| **VIN-04** | **Budget Cloud ridotto:** Le risorse economiche per il deployment sono minime; l'architettura deve essere ottimizzata per girare su un'infrastruttura economica.                                                                                   | Vincoli del progetto            |
| **VIN-05** | **Sviluppo individuale e scadenze:** Il software viene interamente progettato e programmato da un solo sviluppatore, rispettando le date di consegna del corso.                                                                                    | Organizzazione didattica        |

### Dipendenze

| ID         | Risorsa o Attività Esterna                                                                                                            | Scadenza Necessaria                 | Chi se ne occupa                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------- |
| **DIP-01** | Configurazione e attivazione dell'account per il servizio SMTP esterno (es. Brevo) per l'invio delle mail di invito.                  | Prima del collaudo finale           | Sviluppatore (Matteo Braida)                      |
| **DIP-02** | Creazione dell'account sul provider cloud (Hetzner) e inserimento del metodo di pagamento.                                            | Prima del primo rilascio in cloud   | Sviluppatore (Matteo Braida)                      |
| **DIP-03** | Registrazione di un dominio web valido (o sottodominio) con configurazione del certificato SSL per l'HTTPS.                           | Prima del primo rilascio in cloud   | Sviluppatore (Matteo Braida)                      |
| **DIP-04** | Fornitura di un file di esempio anonimizzato della segreteria (es. CSV) per testare l'algoritmo di importazione di studenti e classi. | Prima della fase di test e collaudo | Sviluppatore, in collaborazione con la segreteria |
| **DIP-05** | Prenotazione del laboratorio di informatica della scuola e coordinamento con una classe del primo anno per il test sul campo.         | Giorno stabilito per il collaudo    | Docente del corso                                 |

---

# Seconda parte · Il come

<aside>
💡

Da qui in poi parli al tuo docente e al tuo team, non al Direttore. Ogni scelta tecnica va motivata e confrontata con almeno un'alternativa. "Lo conosciamo" è una motivazione valida, ma non può essere l'unica.

</aside>

## Stima del carico

### Analisi del carico e utenti concorrenti

| Scenario d'uso                       | Utenti attivi simultaneamente | Origine e logica del calcolo                                                                                                                                                                                                          |
| ------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Uso quotidiano standard**          | ~100 utenti                   | Rappresenta circa il 10% degli utenti totali connessi nello stesso momento. Il traffico si concentra principalmente durante la ricreazione e nel pomeriggio a casa, quando i ragazzi controllano i compiti (vedi ASS-06).             |
| **Picco delle ore 9:00 (Verifiche)** | 125 nominali (testato a 150)  | Questo numero è vincolato dai PC effettivamente disponibili nei laboratori per svolgere i test (ASS-02). Ho aggiunto un margine del 20% per sicurezza, come richiesto in NFR-01.                                                      |
| **Scrutini e fine quadrimestre**     | ~200 utenti                   | Si verifica quando quasi tutti i 75 docenti sono online per chiudere i registri e pubblicare i voti finali, causando un picco di accessi immediato da parte degli studenti (~15% della scuola) che entrano a controllare i tabelloni. |

Analizzando i numeri, la quantità assoluta di richieste al secondo (RPS) è ridotta. Al picco delle 9:00, 150 studenti che aprono il quiz nello stesso minuto generano circa 2.5 richieste al secondo sul backend. Durante la prova, il salvataggio automatico delle risposte (FR-VER-03) si traduce in meno di una scrittura al secondo nel database (125 studenti che inseriscono circa 10 risposte spalmate su 50 minuti). Il vero problema tecnologico non è il volume complessivo dei dati, ma la **concorrenza simultanea**: le richieste arrivano tutte nello stesso identico istante e il sistema non deve perdere nemmeno un pacchetto.

### Profilo di carico delle operazioni

| Operazione                      | Frequenza                                 | Impatto Hardware                       | Criticità | Dettagli Tecnici                                                                                                                                                                                                       |
| ------------------------------- | ----------------------------------------- | -------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Autenticazione (Login)**      | Elevata nei cambi ora (8:00 e 9:00)       | Basso, ma rallentato da logica backend | Alta      | L'operazione è resa esplicitamente dispendiosa per la CPU dall'algoritmo di hashing della password (sicurezza base). Il blocco dopo 5 fallimenti (NFR-04) serve a mitigare gli attacchi di brute-force.                |
| **Download e apertura test**    | Concentrata in pochi secondi a inizio ora | Basso (I/O in sola lettura)            | Alta      | È la metrica critica per il requisito NFR-01. Per ottimizzare le performance, tutte le domande del quiz vengono caricate con un'unica query GET iniziale.                                                              |
| **Salvataggio risposta**        | Continua durante tutta la verifica        | Basso (singole scritture mirate)       | Alta      | Ogni risposta parziale viene salvata subito nel DB. Se una scrittura fallisce, lo studente rischia di perdere il testo inserito; per questo motivo la query ha la massima priorità.                                    |
| **Consegna finale compito**     | Concentrata nei minuti finali             | Medio (scrittura e calcolo logico)     | Alta      | Allo scadere del tempo il server forza la consegna massiva delle sessioni rimaste aperte, eseguendo la correzione automatica delle domande a risposta multipla.                                                        |
| **Dashboard del Direttore**     | Bassa (qualche volta a settimana)         | Elevato (CPU e RAM)                    | Bassa     | Questa pagina esegue pesanti query di aggregazione per calcolare le medie di tutte le classi e materie. Essendo una lettura complessa, può richiedere 2-3 secondi senza compromettere l'esperienza degli altri utenti. |
| **Upload materiale didattico**  | Media (distribuita nella giornata)        | Elevato (Banda e Storage)              | Bassa     | I docenti caricano allegati fino a 20 MB. Il processo è pesante per la rete, ma viene gestito quasi sempre al di fuori delle ore di picco dei compiti in classe.                                                       |
| **Importazione studenti (CSV)** | Rara (eseguita solo a inizio anno)        | Elevato (I/O e code mail)              | Bassa     | Elabora centinaia di righe e avvia i processi di notifica. Per evitare colli di bottiglia, l'invio delle mail di invito viene delegato in background a un task periodico (cron) ogni 5 minuti.                         |
|                                 |

<aside>
💡

I numeri di qui devono essere coerenti con la scuola che avete immaginato e con i requisiti non funzionali. Se dichiarate 800 studenti, non potete dimensionare per 20 utenti senza spiegare perché.

</aside>

---

## Scelte tecnologiche e motivazioni

Per lo sviluppo di Omnis Scuola ho scelto strumenti che bilanciano le richieste della traccia con la necessità di completare il progetto da solo, sfruttando quello che stiamo studiando a scuola.

| Area                       | Componente Scelto                                                  | Alternativa Valutata                         | Ragione della Scelta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------- | ------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend**                | **Django** con **Django REST Framework** (Python)                  | Express.js (Node.js)                         | Django ha già pronti i moduli fondamentali che mi servono: la gestione degli utenti, il controllo dei permessi e i comandi per creare le tabelle nel database. Django REST Framework mi aiuta invece a gestire l'invio dei dati in formato JSON e la divisione in pagine (paginazione). Sviluppando il progetto da solo, questo mi fa risparmiare un sacco di tempo e di righe di codice rispetto a Express.js, dove avrei dovuto cercare e configurare librerie esterne per fare ogni singola cosa. |
| **Frontend**               | **React**                                                          | Vue.js                                       | Ho scelto React perché è la tecnologia che stiamo studiando a lezione in questo periodo. In questo modo il progetto mi serve anche come pratica per il corso, senza costringermi a imparare un altro framework da zero. In più, online si trovano moltissimi componenti già pronti e accessibili (vincolo VIN-03).                                                                                                                                                                                   |
| **Database**               | **PostgreSQL**                                                     | MySQL                                        | Sono due database relazionali molto simili e adatti al progetto. Ho preferito PostgreSQL perché si collega molto bene con Django e permette di impostare dei controlli rigidi direttamente sulle tabelle (ad esempio per bloccare i voti fuori dalla scala 1-10), agendo come una sicurezza in più se ci fosse un bug nel codice.                                                                                                                                                                    |
| **Provider Cloud**         | **Hetzner Cloud**                                                  | AWS / Azure                                  | Piattaforme come AWS o Azure hanno costi a consumo difficili da calcolare, e rischierei di sforare il budget (VIN-04). Hetzner ha prezzi fissi al mese molto economici. In più, ha i server in Europa, cosa obbligatoria per le leggi sulla privacy dei minorenni (GDPR).                                                                                                                                                                                                                            |
| **Server e Rilascio**      | Singolo server virtuale (**CPX22**) gestito con **Docker Compose** | Piattaforma automatica (es. Heroku o Render) | Visto che l'app deve gestire circa 200 utenti nei momenti di picco, un solo server virtuale basta e avanza per far girare tutto insieme (database, backend e frontend). Usare Docker mi permette di lavorare sul mio PC in un ambiente identico a quello che ci sarà online, evitando problemi durante il caricamento sul cloud. Le piattaforme automatiche sarebbero costate molto di più.                                                                                                          |
| **Posizione del Server**   | **Germania**                                                       | Helsinki                                     | I server in Germania sono all'interno dell'Unione Europea (per il GDPR) e sono geograficamente più vicini all'Italia. Questo significa che i dati viaggiano più velocemente e le pagine dell'applicazione si caricano prima rispetto a un server in Finlandia.                                                                                                                                                                                                                                       |
| **Servizio Email Esterno** | **Brevo**                                                          | SendGrid                                     | Brevo è un'azienda europea che rispetta il GDPR per la privacy. Il piano gratuito offre 300 email al giorno: per non superare il limite a inizio anno quando si caricano tutti gli studenti insieme, ho impostato il sistema in modo che gli inviti non partano tutti all'istante ma vengano accodati e spediti a blocchi ogni pochi minuti. SendGrid è americana e ha regole sulla privacy più complesse per i dati dei minorenni.                                                                  |
| **Attività in Background** | **Comando Django eseguito ogni 5 minuti (Cron)**                   | Celery con Redis                             | Le attività da fare in background sono minime (inviare la coda di mail e chiudere i compiti scaduti). Usare strumenti complessi come Celery avrebbe complicato inutilmente la struttura del server. Un semplice script programmato sul server che controlla il database ogni 5 minuti è la soluzione più leggera e facile da gestire.                                                                                                                                                                |
| **Documentazione API**     | **drf-spectacular** (OpenAPI 3.0)                                  | drf-yasg                                     | La traccia del progetto chiede obbligatoriamente lo standard OpenAPI 3 (VIN-01). La libreria `drf-spectacular` serve proprio a generare in automatico la pagina di documentazione (Swagger) in versione 3 partendo dal codice Django, mentre l'alternativa `drf-yasg` supporta solo la vecchia versione 2.                                                                                                                                                                                           |

---

## Architettura

### Diagramma dei componenti

_Inserisci qui il diagramma. Deve mostrare i componenti principali e come comunicano._

### I livelli

| Livello                | Cosa fa in Omnis Scuola | Esempio concreto |
| ---------------------- | ----------------------- | ---------------- |
| Presentation / API     | _…_                     | _…_              |
| Application / Business | _…_                     | _…_              |
| Data access            | _…_                     | _…_              |

### Le dipendenze fra i livelli

_Chi può conoscere chi, e in quale direzione. Spiega come questa struttura riduce l'accoppiamento e rende il sistema testabile._

---

## Le API

### Le risorse

_Elenca le risorse REST principali. Es. `/classi`, `/verifiche`, `/voti`._

### Il contratto delle API principali

| Verbo    | Route            | Chi può chiamarla | Payload di esempio                | Risposte previste    |
| -------- | ---------------- | ----------------- | --------------------------------- | -------------------- |
| `POST`   | `*/api/docenti*` | _Direttore_       | `*{ "nome": "…", "email": "…" }*` | _201, 400, 403, 409_ |
| `GET`    | _…_              | _…_               | _…_                               | _…_                  |
| `PUT`    | _…_              | _…_               | _…_                               | _…_                  |
| `PATCH`  | _…_              | _…_               | _…_                               | _…_                  |
| `DELETE` | _…_              | _…_               | _…_                               | _…_                  |

### Errori, validazione e paginazione

**Formato uniforme degli errori.** _Mostra un esempio di risposta di errore._

**Validazione degli input.** _Dove avviene e con quali regole._

**Paginazione.** _Come funziona. Parametri, dimensione di default, formato della risposta._

**Documentazione e verifica.** _Come userete OpenAPI/Swagger e la collezione Postman._

---

## Persistenza e modello dei dati

### Diagramma ER

_Inserisci qui il diagramma entità-relazioni con le cardinalità._

### Identificatori

_Come vengono generati gli ID, e perché. Numeri incrementali, UUID, altro?_

### Tre modelli diversi

| Entità     | Nel database | Nel dominio | Esposta dall'API | Dove differiscono e perché |
| ---------- | ------------ | ----------- | ---------------- | -------------------------- |
| _es. Voto_ | _…_          | _…_         | _…_              | _…_                        |

### Normalizzazione e letture aggregate

_Come è normalizzato il modello. Dove serve una lettura denormalizzata, per esempio la pagina dei voti per materia o la dashboard del Direttore._

### Accesso ai dati

_Strategia di accesso ai dati e uso delle query parametrizzate contro la SQL injection._

---

## Sicurezza e integrazione

### Autenticazione e token

_Come si ottiene il token, cosa contiene, come viaggia il profilo utente._

### Chi può fare cosa

| Operazione                    | Direttore | Docente | Studente |
| ----------------------------- | --------- | ------- | -------- |
| Creare un docente             | ✅        | ❌      | ❌       |
| Caricare materiale            | _…_       | _…_     | _…_      |
| Vedere i voti di uno studente | _…_       | _…_     | _…_      |
| _…_                           |           |         |          |

_Spiega dove viene fatto rispettare questo controllo. Ricorda che il frontend non basta mai._

### L'API esterna

_Quale servizio usate, per cosa, e cosa succede quando non risponde._

### Configurazione e segreti

_Dove vivono connection string e segreti, e come cambiano fra Development e Production._

---

## Qualità architetturale

### Organizzazione del codice

_Struttura di progetti, moduli e cartelle, con le motivazioni._

### Dependency inversion e IoC

_Dove li applicate e a cosa servono in Omnis Scuola._

### Testabilità

_Cosa testerete, e come separate database e API esterne per sostituirli nei test._

### Development e Production

|          | Development | Production |
| -------- | ----------- | ---------- |
| Database | _…_         | _…_        |
| Segreti  | _…_         | _…_        |
| Log      | _…_         | _…_        |
| _…_      |             |            |

---

## Dimensionamento e costi

| Componente       | Servizio | Taglia (CPU, RAM, storage) | Istanze | Costo mensile stimato |
| ---------------- | -------- | -------------------------- | ------- | --------------------- |
| Backend          | _…_      | _…_                        | _…_     | _…_                   |
| Database         | _…_      | _…_                        | _…_     | _…_                   |
| Storage dei file | _…_      | _…_                        | _…_     | _…_                   |
| _…_              |          |                            |         |                       |
| **Totale**       |          |                            |         | **_…_**               |

**Strategia di scalabilità.** _Verticale o orizzontale? Manuale o automatica?_

**Se la stima si rivela sbagliata.** _Cosa fate se gli utenti sono il doppio? E se sono la metà?_

---

## Piano di deployment

_Come Omnis Scuola arriva sul cloud scelto. Come si passa da una versione alla successiva. Come vengono gestite nel tempo le modifiche allo schema del database._

---

# Terza parte · Tempi e valutazione

## Milestone

| Milestone                    | Cosa è pronto    | Data prevista | Responsabile    |
| ---------------------------- | ---------------- | ------------- | --------------- |
| PRD validato                 | Questo documento | _…_           | _tutto il team_ |
| _Prima versione in cloud_    | _…_              | _…_           | _…_             |
| _Collaudo con il primo anno_ | _…_              | _…_           | _…_             |
| _…_                          |                  |               |                 |

<aside>
💡

Stima il tempo di ogni fase come se tutto andasse bene. Poi aggiungi un margine. Non va mai tutto bene.

</aside>

## Piano di valutazione

Come capirete che Omnis Scuola funziona e come validerete che la vostra soluzione sta avendo un impatto positivo?

| Metrica                                                    | Obiettivo | Come la misurate                             | Quando       |
| ---------------------------------------------------------- | --------- | -------------------------------------------- | ------------ |
| _es. Collaudatori che completano una verifica senza aiuto_ | _90%_     | _Osservazione durante il collaudo_           | _Collaudo_   |
| _es. Voti persi_                                           | _0_       | _Confronto fra voti inseriti e voti salvati_ | _Primo mese_ |
|                                                            |           |                                              |              |

---

## Acceptance Criteria di questa PRD

- [ ] Ogni parte rappresentata da questo template ha tutte le sezioni richieste senza saltare nessun punto
- [ ] Avete deciso tutti i punti che la traccia e gli esempi lasciano aperti.
- [ ] Ogni requisito non funzionale ha una soglia e una condizione.
- [ ] Ogni NFR è collegato ad almeno una user story.
- [ ] Avete inserito i requisiti impliciti emersi da interviste che avete fatto.
- [ ] Assunzioni, vincoli e dipendenze sono separati e scritti.
- [ ] I numeri della stima del carico sono coerenti con la scuola immaginata e con il dimensionamento.
- [ ] Ogni scelta tecnica ha almeno un'alternativa scartata e una motivazione.
- [ ] La prima parte non contiene scelte tecniche.
- [ ] Lo storico delle versioni è aggiornato .
