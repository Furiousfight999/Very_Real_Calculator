# IDK
11/13/25
I made the python file mostly work (the mesh network still doesn't work)
why was it failing before? simple. I AM DUMB. I used exec() when i was supposed to used:
import subprocess
then:
subprocess.run(filepath)
i spent like 2 hours not understanding why exec didn't work