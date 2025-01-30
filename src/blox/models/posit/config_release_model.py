from typing import Optional, List, Literal
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ConfigReleaseModel:
	"""
	Immutable dataclass that encapsulates the settings supplied by the user in the config_release.yml file
	"""

	app_dir: Optional[str] = field(default=None, metadata={"description": "Directory of the application"})
	access_type: Optional[Literal["all", "logged_in", "acl"]] = field(default=None, metadata={"description": "Type of access control"})
	viewer_groups: Optional[List[str]] = field(
		default_factory=list,
		metadata={"description": "Groups that can view the application"},
	)
	max_processes: Optional[int] = field(default=None, metadata={"description": "Maximum number of processes"})
	min_processes: Optional[int] = field(default=None, metadata={"description": "Minimum number of processes"})
	max_connections_per_process: Optional[int] = field(default=None, metadata={"description": "Maximum connections per process"})
	load_factor: Optional[float] = field(default=None, metadata={"description": "Load factor for scaling"})
	idle_timeout: Optional[int] = field(default=None, metadata={"description": "Timeout for idle processes"})
	init_timeout: Optional[int] = field(default=None, metadata={"description": "Timeout for initialization"})
	connection_timeout: Optional[int] = field(default=None, metadata={"description": "Timeout for connections"})
	read_timeout: Optional[int] = field(default=None, metadata={"description": "Timeout for reading data"})
	memory_request: Optional[int] = field(default=None, metadata={"description": "Memory request for the application"})
	memory_limit: Optional[int] = field(default=None, metadata={"description": "Memory limit for the application"})
	run_time_image: Optional[str] = field(default=None, metadata={"description": "Runtime image for the application"})
	threads: Optional[int] = field(default=None, metadata={"description": "Number of threads"})
	loops: Optional[int] = field(default=None, metadata={"description": "Number of loops"})
	delay_per_request: Optional[int] = field(default=None, metadata={"description": "Delay per request"})
	response_time_median_threshold: Optional[int] = field(default=None, metadata={"description": "Median threshold for response time"})
	run_as_user: Optional[str] = field(default=None, metadata={"description": "User to run the application as"})
	app_name: Optional[str] = field(default=None, metadata={"description": "Name of the application"})
	vanity_url: Optional[str] = field(default=None, metadata={"description": "Vanity URL for the application"})
	collaborator_groups: Optional[List[str]] = field(
		default_factory=list,
		metadata={"description": "Groups that can collaborate on the application"},
	)
