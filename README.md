
L1Trigger-L1TMuonEndCap
=======

Repository for holding the CMS EMTF BDT LUT. Each xml represents one tree in the forest with 400 trees for each EMTF mode. 

Versions
--------

* `v0p0`
    * Initial training with incorrect xmls due to bug in original code. 
    * Run2 w/ Run2 variables without bit compression

* `v0p1`      
    * Initial trainnig with correct xmls after fixing bug
    * Run2 w/ Run2 variables without bit compression 

* `v0p2`
    * Training with bit compression 
    * Run2 w/ Run2 variables with bit compression 

* `v0p3`
    * Training with bit compression and no RPCs -  to test rate anomoly 
    * Run2 w/ Run2 variables with bit compression and with RPCs off 

* `v2p0`
    * Training with new sample that is properly flat in 1/pT
    * Run2 w/ Run2 variables with bit compression

