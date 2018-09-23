# AWS parameter store
if [ "$AWS_ENVIROMENT" == "hml"]
then
echo -ne "Loading variables from Parameter Store:\n"
echo -ne "------------------------------\n\n"
echo -ne "AWS_ENVIROMENT=\"$AWS_ENVIROMENT\"\n"
echo -ne "AWS_APP=\"$AWS_APP\"\n"
echo -ne "AWS_REGION=\"$AWS_REGION\"\n"
echo -ne "\n"

aws ssm get-parameters --name $AWS_ENVIROMENT.$AWS_APP --with-decryption --region $AWS_REGION | jq --raw-output .Parameter[0].Value ?
> /home/oyaji/.env

fi

# verify files
echo -ne "Files on /home/oyaji:\n"
echo -ne "------------------------------\n\n"
echo -ne "$(ls -lah /home/oyaji)\n"
echo -ne "\n"


# Load environment vars from .env file
for ENVVAR in $(cat /home/oyaji/.env)
do 
    export $ENVVAR
done

export APP_DEFAULT_PORT=80
export DEBUG=False
export AUTO_RELOAD=False
export APP_DEFAULT_HOST=0.0.0.0

echo -ne "Running.....\n"
echo -ne "------------------------------\n\n"

python application.py
