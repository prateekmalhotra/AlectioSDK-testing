import os

if __name__ == '__main__':

	# STEP 1: Successfully installing the SDK
	os.system('python3 -m virtualenv env')

	activator = 'env/bin/activate_this.py'
	with open(activator) as f:
		exec(f.read(), {'__file__': activator})

	os.system('python3 -m pip install -r requirements.txt')
	os.system('sh scripts/sdk_install.sh')

	# STEP 2: FE
	os.system('python3 -B scripts/fe.py')

	# STEP 3: Execute steps for your example
	os.system('sh examples/image_classification/cifar10/cifar10.sh')
