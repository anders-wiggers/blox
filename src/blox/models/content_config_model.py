from typing import Optional, Literal

class ContentSettings:
    def __init__(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        access_type: Optional[Literal['all', 'logged_in', 'acl']] = 'acl',
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
