small-1/2/3/bpo folders contains input and (some) output files that we have used in our calculations.
pdos-1/2/3/bpo folders contains the pdos output that we have done and used for our manuscript.
pseudo.zip is the general file for all materials in this work and contains pseudopotentials used for our work. Make sure to update the pseudopotential directory in the input files to run the task properly.
Change the 'BPBO' below into 'BPO' for BPO calculation instead

#QE band structure
pw.x -in BPBO.scf.in > BPBO.scf.out
pw.x -in BPBO.nscf.in2 > BPBO.nscf.out
bands.x -in BPBO.bands.in > BPBO.bands.out

#QE projection density of states
pw.x -in BPBO.scf.in > BPBO.scf.out
pw.x -in BPBO.nscf.proj.in > BPBO.nscf.proj.out
projwfc.x -in BPBO.projwfc.in > BPBO.projwfc.out

#QE + W90 for spin Hall conductivity
pw.x -in BPBO.scf.in > BPBO.scf.out
pw.x -in BPBO.nscf.in2 > BPBO.nscf.out
cp BPBO.win1 BPBO.win
wannier90.x -pp BPBO
pw2wannier90.x -in BPBO.pw2wan.in > BPBO.pw2wan.out
%cp BPBO.win1 BPBO.win                          # remove the '%' for SHC fermiscan calculation
%cp BPBO.win4 BPBO.win                          # remove the '%' for electrical conductivity calculation
wannier90.x BPBO
postw90.x BPBO
