from enum import StrEnum
from typing import Optional, Literal


class Config(StrEnum):
	"""
	Enum for the keys in the config_release.yml file
	"""

	NAME = "name"
	DESCRIPTION = "description"
	ACCESS_TYPE = "access_type"
	TITLE = "title"
	CONNECTION_TIMEOUT = "connection_timeout"
	READ_TIMEOUT = "read_timeout"
	INIT_TIMEOUT = "init_timeout"
	IDLE_TIMEOUT = "idle_timeout"
	MAX_PROCESSES = "max_processes"
	MIN_PROCESSES = "min_processes"
	MAX_CONNS_PER_PROCESS = "max_conns_per_process"
	LOAD_FACTOR = "load_factor"
	CPU_REQUEST = "cpu_request"
	CPU_LIMIT = "cpu_limit"
	MEMORY_REQUEST = "memory_request"
	MEMORY_LIMIT = "memory_limit"
	AMD_GPU_LIMIT = "amd_gpu_limit"
	NVIDIA_GPU_LIMIT = "nvidia_gpu_limit"
	RUN_AS = "run_as"
	RUN_AS_CURRENT_USER = "run_as_current_user"
	DEFAULT_IMAGE_NAME = "default_image_name"
	DEFAULT_R_ENVIRONMENT_MANAGEMENT = "default_r_environment_management"
	DEFAULT_PY_ENVIRONMENT_MANAGEMENT = "default_py_environment_management"
	SERVICE_ACCOUNT_NAME = "service_account_name"
	EXTENSION = "extension"


class PositContentSettings:
	"""
	Encapsulates the settings for a content object in Posit
	"""

	name: Optional[str] = None
	description: Optional[str] = None
	access_type: Optional[Literal["all", "logged_in", "acl"]] = "acl"
	title: Optional[str] = None
	connection_timeout: Optional[int] = None
	read_timeout: Optional[int] = None
	init_timeout: Optional[int] = None
	idle_timeout: Optional[int] = None
	max_processes: Optional[int] = None
	min_processes: Optional[int] = None
	max_conns_per_process: Optional[int] = None
	load_factor: Optional[float] = None
	cpu_request: Optional[float] = None
	cpu_limit: Optional[float] = None
	memory_request: Optional[int] = None
	memory_limit: Optional[int] = None
	amd_gpu_limit: Optional[float] = None
	nvidia_gpu_limit: Optional[float] = None
	run_as: Optional[str] = None
	run_as_current_user: Optional[bool] = False
	default_image_name: Optional[str] = None
	default_r_environment_management: Optional[bool] = None
	default_py_environment_management: Optional[bool] = None
	service_account_name: Optional[str] = None
	extension: Optional[bool] = None

	def __init__(
		self,
		name: Optional[str] = None,
		description: Optional[str] = None,
		access_type: Optional[Literal["all", "logged_in", "acl"]] = "acl",
		title: Optional[str] = None,
		connection_timeout: Optional[int] = None,
		read_timeout: Optional[int] = None,
		init_timeout: Optional[int] = None,
		idle_timeout: Optional[int] = None,
		max_processes: Optional[int] = None,
		min_processes: Optional[int] = None,
		max_conns_per_process: Optional[int] = None,
		load_factor: Optional[float] = None,
		cpu_request: Optional[float] = None,
		cpu_limit: Optional[float] = None,
		memory_request: Optional[int] = None,
		memory_limit: Optional[int] = None,
		amd_gpu_limit: Optional[float] = None,
		nvidia_gpu_limit: Optional[float] = None,
		run_as: Optional[str] = None,
		run_as_current_user: Optional[bool] = False,
		default_image_name: Optional[str] = None,
		default_r_environment_management: Optional[bool] = None,
		default_py_environment_management: Optional[bool] = None,
		service_account_name: Optional[str] = None,
		extension: Optional[bool] = None,
	):
		self.name = name  # A URL-friendly identifier
		self.title = title  # The title of the content
		self.description = description  # A rich description of the content
		self.access_type = access_type  # How content manages viewers
		self.connection_timeout = connection_timeout  # Max seconds without data sent/received
		self.read_timeout = read_timeout  # Max seconds without data from a client connection
		self.init_timeout = init_timeout  # Max seconds for an interactive app to start
		self.idle_timeout = idle_timeout  # Max seconds a worker process can stay idle
		self.max_processes = max_processes  # Max concurrent processes allowed
		self.min_processes = min_processes  # Min concurrent processes allowed
		self.max_conns_per_process = max_conns_per_process  # Max connections per process
		self.load_factor = load_factor  # Controls new process spawning
		self.cpu_request = cpu_request  # Min compute power in "CPU Units"
		self.cpu_limit = cpu_limit  # Max compute power in "CPU Units"
		self.memory_request = memory_request  # Min RAM required in bytes
		self.memory_limit = memory_limit  # Max RAM allowed in bytes
		self.amd_gpu_limit = amd_gpu_limit  # Number of AMD GPUs allocated
		self.nvidia_gpu_limit = nvidia_gpu_limit  # Number of NVIDIA GPUs allocated
		self.run_as = run_as  # The UNIX user executing the content
		self.run_as_current_user = run_as_current_user  # Run processes under visiting user's account
		self.default_image_name = default_image_name  # Default image used for execution
		self.default_r_environment_management = default_r_environment_management  # Manage R environment
		self.default_py_environment_management = default_py_environment_management  # Manage Python environment
		self.service_account_name = service_account_name  # Kubernetes service account name
		self.extension = extension  # Whether the content is a Connect Extension
