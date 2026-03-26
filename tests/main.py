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
    except Exception as e:
        logging.error(f"Error performing {args.action}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()