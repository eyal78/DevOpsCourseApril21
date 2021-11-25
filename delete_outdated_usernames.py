import boto3
from botocore.exceptions import ClientError
from get_user_age_seconds import get_user_age_seconds
from termcolor import colored
from yes_or_no import yes_or_no
import time
client = boto3.client('iam')

#TODO Define Admin UserName To be ignored
admin = "noamsint"

#TODO Define Policy To Delete From Expired Users
user_policy = 'arn:aws:iam::955114013936:policy/S3VideoReader'



def delete_outdated_usernames():

    # Asking If To Print Of List Of Users After Deletion
    yes_or_no("Would You Like To Print A list Of Users After Deletion?")

    # Deletes users older than max_user_age_seconds
    while True:
                client = boto3.client('iam')

                iam = boto3.resource('iam')

                policy = iam.Policy(user_policy)

                response = client.list_users()


                users_d = (response['Users'])


                for x in range(len(users_d)):
                    fo_user = users_d[x]['UserName']
                    expired = get_user_age_seconds(fo_user)
                    if expired == True and fo_user != admin:

                        try:
                            print("Trying To Detach User '{} ' From Policy...".format(fo_user))
                            print("--------------------------------------------")
                            response_policy = policy.detach_user(
                                UserName=fo_user)
                            time.sleep(2)
                            
                        except client.exceptions.NoSuchEntityException :
                            print('Policy Was Not Found')
                            print("--------------------------------------------")
                            time.sleep(2)



                        """
                        try:
                            print("Trying to Delete Access Key")
                            response_del_acc = client.delete_access_key(
                            AccessKeyId='AKIA54YJ3ITYDA3JMFOU',
                            UserName=fo_user,)
                            print(response_del_acc)
                        except ClientError as e:
                            print("Unexpected error: %s" % e)
                        """

                        try:
                            print((colored("Trying To Delete User '{}'...".format(fo_user), 'yellow')))
                            print("--------------------------------------------")
                            response_del = client.delete_user(
                                UserName=fo_user
                            )
                            time.sleep(2)
                            print((colored("Deleted Successfully '{}'".format(fo_user), 'green')))
                            print("--------------------------------------------")
                            time.sleep(2)
                        except ClientError as e:
                            print("Unexpected error: %s" % e)
                            time.sleep(2)




                    if yes_or_no == True:
                        print("Getting users from IAM...")
                        response = client.list_users()
                        for x in response['Users']:
                            print(x['UserName'])
                            time.sleep(3)
                            continue
                else:
                        continue




