HEAD_IP = "x.x.x.x"
HEAD_PORT = 5050
HEAD_BIND_IP = "0.0.0.0"

CONTROLLER_PORT = 5151
CONTROLLER_BIND_IP = "0.0.0.0"

PERSISTENT_REFRESH = 60
RUNTIME_REFRESH = 4

HEARTBEAT_INTERVAL = 5
DECISION_INTERVAL = 15
MAX_HB_HISTORY = 10
MAX_AVG_LOAD = 0.80
MIN_AVG_LOAD = 0.40
MIN_MEASURE_LOAD_HB = 3 # <= MAX_HB_HISTORY
MAX_AVG_TIME = 30
MIN_AVG_TIME = 15


MAX_WORKERS = 10
WORKER_CREDIT = 3

MAX_STARTUP_TIME = 300
MIN_SCALE_INTERVAL = MAX_STARTUP_TIME
MAX_SHUTDOWN_TIME = 120
MAX_TRANSITION_TIME = DECISION_INTERVAL*2

APOLLO_API_PORT = 61680
APOLLO_QUEUE_PORT = 61613
APOLLO_USER = "admin"
APOLLO_PASSWORD = "password"
APOLLO_DEST = "/queue-name"

VM_IMAGE_DIR = "VM image dir that contains the x.one file for opennebula"

PRODUCER_IMG_URL = "http://example.com/x.pjg"
MAX_WORKER_AVERAGE = 10
MAX_WORKER_THREAD_HISTORY = 3
