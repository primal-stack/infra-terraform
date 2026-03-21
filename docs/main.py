import os
import sys
from pathlib import Path

from infra_terraform.main import Terraform

def main():
    if len(sys.argv)!= 2:
        print("Usage: python main.py <action>")
        sys.exit(1)

    action = sys.argv[1]

    if action not in ['apply', 'destroy', 'plan', 'init']:
        print("Invalid action. Choose from: apply, destroy, plan, init")
        sys.exit(1)

    terraform = Terraform()

    if action == 'init':
        terraform.init()
    elif action == 'apply':
        terraform.apply()
    elif action == 'destroy':
        terraform.destroy()
    elif action == 'plan':
        terraform.plan()

if __name__ == "__main__":
    main()