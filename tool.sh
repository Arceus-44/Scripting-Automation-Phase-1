
#!/bin/bash

# Tool Name: System Information Tool
# Objective: Display basic Linux system information

show_help() {
    echo "Usage: ./tool.sh [--help]"
    echo "Displays basic system information."
}

# Handle help option
if [[ "$1" == "--help" ]]; then
    show_help
    exit 0
fi

echo "===== System Information Tool ====="

echo "Hostname:"
hostname

echo ""
echo "Current User:"
whoami

echo ""
echo "Operating System:"
uname -s

echo ""
echo "Kernel Version:"
uname -r

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "===== Scan Complete ====="
