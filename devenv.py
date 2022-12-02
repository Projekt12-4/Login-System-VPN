import os
from dataclasses import dataclass, field

@dataclass(kw_only=True, frozen=True)
class DevEnvSetup():

    container    
