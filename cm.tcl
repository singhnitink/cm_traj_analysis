mol new em.gro
mol addfile viz1.xtc step 10 waitfor all
set nframes [molinfo top get numframes]
puts "*********************************"
puts "Total number of frames is ${nframes}"
puts "*********************************"


set outfile1 [open "contact_map_simulation.dat" w]

for {set i 0} {$i < $nframes} {incr i} {
	puts $i
	set sel [atomselect top "name CA"]
	set resids [$sel get {resid}]
  foreach resid $resids {
	    set a [atomselect top "(protein and noh) and (within 6 of (protein and resid $resid and noh))"]
      set b [$a get {resid}]
      puts $outfile1 [format "%d \t %s " $resid $b]
   }
}
close $outfile1
mol delete all
exit
