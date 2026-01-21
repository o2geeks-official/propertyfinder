from pydantic_settings import BaseSettings


class ResponseMessages(BaseSettings):
    LIMIT_EXCEEDED: str = "Limit exceeded"
    RECORD_ALREADY_EXIST: str = "Record already exist"
    INVALID_ID: str = "Invalid value"
    INVALID_PARENT_CATEGORY_ID: str = "Invalid parent category id"
    INVALID_USER_ID: str = "Invalid user id"
    DUPLICATE_CONTENT: str = "Item with same name already exists"
    VALUE_UPDATED: str = "Value has been updated successfully"
    VALUE_ADDED: str = "Value has been added successfully"
    VALUE_DELETED: str = "Value has been deleted successfully"
    MISMATCH_VALUES: str = "Values does not match with each other"
    EMAIL_NOT_FOUND: str = "unable to find email for login, please signup"
    INVALID_CREDENTIALS: str = (
        "Could not validate credentials. Please use valid token or re-login"
    )
    INVALID_EMAIL_FORGET: str = "Invalid email address. Please ensure your email is entered in lowercase letters."

    DEACTIVATED_USER: str = "User is deactivated. Please contact administrator"
    MISSING_INVITE_CODE: str = "Invite code is missing. You can get it from your friend"
    INVALID_SIGNUP_UNI: str = "Unfortunately, your university is not in our list. Please contact us at help@edyou.io"
    VALUE_DOES_NOT_EXISTS: str = "Item or record does not exists"
    GROUP_DOES_NOT_EXISTS_OR_YOU_ALREADY_MEMBER: str = "Group does not exists or you are already a member or you have already sent a request or your invitation is pending"
    INSUFFICIENT_PERMISSIONS: str = "User does not have sufficient permissions"
    INSUFFICIENT_PERMISSIONS_CALL_ROOM: str = (
        "User does not have sufficient permissions to call in this room"
    )
    NO_USER_EXISTS_IN_ROOM: str = "No user exists in this room"
    MISSING_VALUES: str = "required values are missing"
    MISSING_SCHOOL_VALUES: str = "School id is missing, please provide school id"
    PASSWORD_CHANGED: str = "Password successfully updated."
    PROFILE_CHANGED: str = "Profile successfully updated."
    USER_DOES_NOT_EXISTS: str = "User with this email does not exists."
    USER_ALREADY_EXISTS: str = "User with this email Already exist."
    MISSING_BEARER_TOKEN: str = "Bearer token is missing in header."
    INVALID_TOKEN_OR_USER: str = "Invalid token or code"
    DB_ERROR: str = "Unable to perform DB ops, Contact Admin"
    INVALID_PASSWORD: str = "Invalid password."
    INVALID_USERNAME_OR_PASSWORD: str = "Invalid username or password."
    EXPIRED_BEARER_TOKEN: str = (
        "Bearer Token is either missing,invalid or expired. Please consider re-login"
    )
    INVALID_IMAGE_MIME: str = "Invalid file mime-type are allowed"
    UNAUTHORIZED_USER: str = "Unauthorized: user does not have permissions to access this page. Please contact administrator"
    MAIL_SUCCESS: str = "Successfully Send Email"
    MAIL_FAILED: str = "Failed to send Email"
    START_MAIL_SERVER_FAILED: str = "Please Start Mail Server First"
    INVALID_EMAIL: str = "Invalid email address"
    RESET_SUCCESS: str = "Reset link successfully sent to your mail id"
    RESET_FAILED: str = "Failed to send Reset link on your mail id"
    APIKEY_SUCCESS: str = "API key successfully generated"
    API_UPDATE: str = "Successfully Updated your Data"
    APIKEY_FAILED: str = "Failed to generate API key"
    INVALID_MIME_TYPE: str = "Only html files are allowed"
    TEMPLATE_UPLOAD_SUCCESS: str = "Template Upload Successfully"
    TEMPLATE_NOTE_FOUND: str = "Template Not Found"
    EVENT_ADD_SUCCESS: str = "Event Add Successfully"
    EVENT_ADD_FAILED: str = "Failed To Add Event"
    COVER_PHOTO_SUCCESS: str = "Cover Photo Saved Successfully"
    EVENT_DELETE_SUCCESS: str = "Event Delete Successfully"
    EVENT_DELETE_FAILED: str = "Event Deletion Failed"
    EVENT_UPDATE_SUCCESS: str = "Event Update Successfully"
    EVENT_UPDATE_FAILED: str = "Failed To Update Event"
    EVENT_LOAD_SUCCESS: str = "Event Load Successfully"
    EVENT_LOAD_FAILED: str = "Failed To Load Event"
    GROUP_ADD_SUCCESS: str = "Event Added in a Group"
    GROUP_ADD_FAILED: str = "Failed To Add Event in a Group"
    POST_Delete_SUCCESS: str = "Post Deleted Successfully"
    FRIENDS_LOAD_SUCCESS: str = "Friends Data Load Successfully"
    FRIENDS_LOAD_FAILED: str = "Failed to load friends Data"
    FRIENDS_REQUEST_FAILED: str = (
        "Failed to send friend request. Maybe you already made a request"
    )
    FRIENDS_REQUEST_UNAUTHORISED: str = (
        "Only receiver of request can change request status"
    )
    POST_DELETE_FAILED: str = "Failed To Delete Your Post"
    POST_LOAD_FAILED: str = "Failed To Load Your Post"
    GROUP_CREATE_SUCCESS: str = "Group Created Successfully"
    GROUP_CREATE_FAILED: str = "Failed To Create Group"
    GROUP_DELETE_SUCCESS: str = "Group Deleted Successfully"
    GROUP_SAME_NAME: str = "Group with same name already exists"
    GROUP_DELETE_FAILED: str = "Failed To delete Group"
    GROUP_ADMIN_DELETE_FAILED: str = "Group must contain at least one admin"
    GROUP_DOES_NOT_EXISTS_OR_ALREADY_MEMBER: str = (
        "Either Group with this id does not exists or user is already a member"
    )
    GROUP_DOES_NOT_EXISTS_OR_MEMBER_HAVE_NO_PERMISITION: str = (
        "Either Group with this id does not exists or user does not have rights"
    )
    GROUP_POST_FAILED: str = "Failed To Add Post in a Group"
    POST_NOT_FOUND: str = "Post Not Found"
    COMMENT_DELETE_FAILED: str = "Failed to delete Comment"
    ROOM_CREATION_FAILED: str = "Failed To Create RoomInDB"
    PUBLIC_ROOM_NOT_FOUND: str = "Public RoomInDB Not Found"
    GUEST_LIMIT_REACHED: str = "Guest Limit Exceed"
    ROOM_USER_ADD_SUCCESS: str = "This User is already a member"
    ROOM_NOT_FOUND: str = "RoomInDB Not exist"
    MISSING_REQUIRED_PARAMETER: str = "missing required parameter in query"
    ONLY_FRIEND_CAN_VIEW: str = (
        "Sorry it seems you are not friend, Only friends can view this content"
    )
    SUCCESSFULLY_UPDATED: str = "value updated successfully"
    SUCCESSFULLY_ADDED: str = "value added successfully"
    SUCCESSFULLY_DELETED: str = "value deleted successfully"
    SUCCESSFULLY_CAN_BE_VERIFIED: str = "Email can be verified successfully."
    SUCCESSFULLY_CAN_NOT_BE_VERIFIED: str = "Verification code is not valid."
    SUCCESSFULLY_REMOVED: str = "user unblocked successfully"
    # Invite
    MAX_LIMIT_EXCEEDED: str = "Max limit exceeded"
    USER_ALREADY_INVITED: str = (
        "user already invited with this email address or phone number"
    )
    REFERRAL_ALREADY_USED: str = "referral code already used"
    INVITE_WAIT_LIST: str = "Your Account is verified and you are in wait list. You will be notified once you are in"
    EMAIL_NOT_VERIFIED: str = (
        "Your email is not verified. Please verify your email first"
    )
    REFERRAL_INVALID: str = "Invite code is invalid"
    # Waitlist
    EMAIL_ALREADY_EXISTS_IN_WAITLIST: str = (
        "A record against this email already exists in wait-list"
    )
    INVITE_MESSAGE: str = "I'm inviting you to EDYOU, the private app for college life. Download app in Apple Store and use my special code"


response_message = ResponseMessages()
