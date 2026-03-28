import os
import sys
import logging
from argparse import ArgumentParser
from terraform import Terraform

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = ArgumentParser(description="Manage Terraform infrastructure.")
    parser.add_argument('--action', choices=['apply', 'destroy', 'plan'], required=True, help='Terraform action to perform')
    parser.add_argument('--config', default='config.tf', help='Path to Terraform configuration file')
    return parser.parse_args()

def main():
    args = parse_args()
    terraform = Terraform(config_file=args.config)

    try:
        if args.action == 'apply':
            terraform.apply()
        elif args.action == 'destroy':
            terraform.destroy()
        elif args.action == 'plan':
            terraform.plan()
        else:
            logging.error("Invalid action specified. Please choose from 'apply', 'destroy', or 'plan'.")
            sys.exit(1)
    except Exception as e:
        logging.error(f"Error performing {args.action}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

```python
import logging
from argparse import ArgumentParser
from terraform import Terraform

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InfrastructureManager:
    def __init__(self, config_file='config.tf'):
        self.terraform = Terraform(config_file=config_file)

    def apply(self):
        try:
            self.terraform.apply()
        except Exception as e:
            logging.error(f"Error applying configuration: {e}")
            sys.exit(1)

    def destroy(self):
        try:
            self.terraform.destroy()
        except Exception as e:
            logging.error(f"Error destroying infrastructure: {e}")
            sys.exit(1)

    def plan(self):
        try:
            self.terraform.plan()
        except Exception as e:
            logging.error(f"Error creating plan: {e}")
            sys.exit(1)

def main():
    parser = ArgumentParser(description="Manage Terraform infrastructure.")
    parser.add_argument('--action', choices=['apply', 'destroy', 'plan'], required=True, help='Terraform action to perform')
    parser.add_argument('--config', default='config.tf', help='Path to Terraform configuration file')
    args = parser.parse_args()

    infrastructure_manager = InfrastructureManager(config_file=args.config)

    if args.action == 'apply':
        infrastructure_manager.apply()
    elif args.action == 'destroy':
        infrastructure_manager.destroy()
    elif args.action == 'plan':
        infrastructure_manager.plan()
    else:
        logging.error("Invalid action specified. Please choose from 'apply', 'destroy', or 'plan'.")
        sys.exit(1)

if __name__ == "__main__":
    main()