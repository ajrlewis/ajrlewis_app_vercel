# Neuralead

![Neuralead Logo](images/neuralead-logo.svg)

## About

API backend (https://api.neuralead.ai) for Hyperhumans Neuralead Software (https://neuralead.ai/)

## Git Flow

Three branches are used:

  - feature
    - This branch we use for building and testing new features.
  - main
    - This branch is used for merging new features to test system as a whole.
  - live
    - If build tests successfully run on main, then a pull request should be made to the production, i.e. live, branch.

### Deploying to live

1. Go to https://github.com/hyperhumans/neuralead-server-app/pulls
2. Create a **New pull request**
3. Compare changes from **base**: *live* to **compare**: *main*
4. Submit a **Create pull request**
5. **Add a title** of *Live* and copy commit message to **Add a description**
6. Submit a **Create pull request** again.
7. Submit a **Merge pull request**
8. Finally, submit a **Confirm merge**

You should see the revision created for the pull request here within 10 minutes:
https://console.cloud.google.com/run/detail/europe-west1/neuralead-server-app/revisions?inv=1&invt=AbislQ&project=totemic-fact-428909-t4

## Environmental Variables

| Name                    | Description                                             |
| :-----------------------| :------------------------------------------------------ |
| LOGURU_LEVEL            | https://loguru.readthedocs.io/en/stable/api/logger.html |
| DATABASE_URL            | Database connection string                              |
| BLOB_READ_WRITE_TOKEN   | Vercel blob storage token                               | 
| BING_WEB_SEARCH_API_KEY | API key for Bing web search                             |
| OPENAI_API_KEY          | API key for OpenAI                                      |
| ROCKET_REACH_API_KEY    | API key for Rocket Reach                                |
| HUNTER_API_KEY          | API key for Hunter.io                                   |

## Bash Scripts

| Name                    | Description                                             |
| :-----------------------| :------------------------------------------------------ |
| clean.sh        | |
| install.sh      | |
| migrate.sh      | |
| wsgi.sh         | | 
| unit_tests.sh   | |
| run_client.sh   | |

## Google Cloud Application

### Application

The application is 

https://console.cloud.google.com/run/detail/europe-west1/neuralead-server-app/metrics?project=totemic-fact-428909-t4&inv=1&invt=Abh6fw

### Environmental Variables

https://console.cloud.google.com/run/deploy/europe-west1/neuralead-server-app?project=totemic-fact-428909-t4&inv=1&invt=Abiglg

https://console.cloud.google.com/security/secret-manager?referrer=search&inv=1&invt=Abiglg&project=totemic-fact-428909-t4

### Log Explorer

https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fconsole.cloud.google.com%2Flogs%2Fquery%3Bduration%3DPT1H%3Freferrer%3Dsearch%26inv%3D1%26invt%3DAbh5MQ%26project%3Dknokd-412220&followup=https%3A%2F%2Fconsole.cloud.google.com%2Flogs%2Fquery%3Bduration%3DPT1H%3Freferrer%3Dsearch%26inv%3D1%26invt%3DAbh5MQ%26project%3Dknokd-412220&osid=1&passive=1209600&service=cloudconsole&ifkv=AcMMx-c9ApARDsxJyoWmAxAi_UTKwM2J92UTDYQd7yRhuJn2ocaBuAnjQYfgcX22ezwaUoa2ARU1dQ&ddm=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin

### SQL Storage

https://console.cloud.google.com/sql/instances/neuralead-postgres/studio?inv=1&invt=AbhzpQ&project=totemic-fact-428909-t4

Database: postgress
User: postgress
Password: ****

### Blob Storage

https://console.cloud.google.com/storage/browser/neuralead-bucket;tab=objects?project=totemic-fact-428909-t4&prefix=&forceOnObjectsSortingFiltering=false&inv=1&invt=Abh51Q

### Migrations

## Company

### Schema

#### Company

| Key       | Type    |              |
| :-------- | :------ |:------------ |
| id        | Integer | primary key  |
| name      | String  | nullable     |
| summary   | String  | nullable     |
| industry  | String  | nullable     |
| keywords  | String  | nullable     |
| headcount | String  | nullable     |
| url       | String  | unique       |
| domain    | String  | nullable     |
| email     | String  | nullable     |
| linkedin  | String  | nullable     |
| twitter   | String  | nullable     |
| facebook  | String  | nullable     |
| linkedin  | String  | nullable     |
| instagram | String  | nullable     |
| youtube   | String  | nullable     |
| location  | String  | nullable     |
| phone     | String  | nullable     |

#### CompanyCompany

| Key       | Type    |               |
| :-------- | :------ |:------------- |
| parent_id   | Integer | primary key, foreign key |
| child_id    | Integer | primary key, foreign key |
| similarity  | Float   | nullable    |

#### UserCompany

| Key       | Type    |              |
| :-------- | :------ |:------------ |
| user_company_id | Integer | primary_key |
| user_id         | Integer | foreign key |
| company_id      | Integer | foreign key | 
| is_accepted     | Boolean | default false |

### API Overview

| Method  | Endpoint                   | Description                                      |
| :-------| :------------------------- |:------------------------------------------------ |
| GET     | /company/                  | Returns all companies.                           |
| GET     | /company/<company_id>      | Returns a specific company.                      |
| POST    | /company/build             | Builds a company from a supplied URL.            |
| POST    | /company/find              | Finds companies based on supplied parameters.    |
| POST    | /company/<company_id>/find | Finds companies based on specific company.       |

### Curl Examples

#### Build and Accept a Company Profile

The following example builds a company profile from a supplied `url` value. The method adds the built company to the `Company` table and accepts the company in the `UserCompany` table. It deducts credits from the current user in the `User` table. Because the company is accepted a full snippet of the company is returned.

```bash 
curl \
--location 'https://api.neuralead.ai/company/build' \
--request POST \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "url": "hyperhumans.ai"
}'
```

```json
{
  "data": {
    "company": {
      "children": [],
      "company_id": 1,
      "domain": "hyperhumans.ai",
      "email": "info@hyperhumans.ai",
      "employees": [],
      "facebook": null,
      "headcount": "1-10",
      "industry": "Artificial Intelligence, Software Development, Technology",
      "instagram": null,
      "is_accepted": true,
      "keywords": "A.I. interfaces, software ecosystem, 4th industrial revolution, beta testing program",
      "linkedin": "https://linkedin.com/company/gradivis-llc",
      "location": "Tallinn, Estonia",
      "name": "Hyperhumans",
      "phone": null,
      "summary": "Hyperhumans is a group of exceptional individuals deploying code for the fourth industrial revolution. They are building an ecosystem of software that will help elevate and evolve human life in business and beyond.",
      "twitter": "https://twitter.com/hyperhumans",
      "url": "https://hyperhumans.ai",
      "youtube": null
    }
  }
}
```

#### Find a Similar Company

The following route finds an `amount` (`1 <= amount <= 5`) of similar companies to a given `company_id`. The method adds the found companies to the `company` table and each each company to the `user_company` but with `is_accepted = False`. The `company_company` table is also updated where the `parent_id` is set to `company_id` supplied and each `child_id` is set to the ID of a found company. Because the found companies have not yet been accepted, only a snippet of their data is returned.

```bash
curl \
--location https://api.neuralead.ai/company/<company_id>/find \
--request POST \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
   "amount": 1
}'
```

```json
{
  "data": {
    "companies": [
      {
        "children": [],
        "company_id": 2,
        "employees": [],
        "is_accepted": false,
        "name": "Bolt",
        "summary": "Bolt is the first European mobility super-app offering better alternatives for every purpose a private car serves, including ride-hailing, shared cars, scooters, and food and grocery delivery."
      }
    ]
  }
}
```

#### Getting Companies

A get request returns all companies that are associated to the given user in the `UserCompany` table. If they have been accepted then the full data are returned otherwise only a snippet is returned. All companies returned contain their `children`, i.e. their similar companies, and `employees`, i.e. employees that are part of that company. A query string, i.e. `?industry=Software`, can be applied to the end of the URL to filter the results or `/<copmany_id>` can be applied to end of the URL to select a specific company.

```bash
curl \
--location 'https://api.neuralead.ai/company' \
--request GET \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

```json
{
  "data": {
    "companies": [
      {
        "children": [
          {
            "company_id": 2,
            "is_accepted": false,
            "name": "Bolt",
            "similarity": null,
            "summary": "Bolt is the first European mobility super-app offering better alternatives for every purpose a private car serves, including ride-hailing, shared cars, scooters, and food and grocery delivery."
          }
        ],
        "company_id": 1,
        "domain": "hyperhumans.ai",
        "email": "info@hyperhumans.ai",
        "employees": [],
        "facebook": null,
        "headcount": "1-10",
        "industry": "Artificial Intelligence, Software Development, Technology",
        "instagram": null,
        "is_accepted": true,
        "keywords": "A.I. interfaces, software ecosystem, 4th industrial revolution, beta testing program",
        "linkedin": "https://linkedin.com/company/gradivis-llc",
        "location": "Tallinn, Estonia",
        "name": "Hyperhumans",
        "phone": null,
        "summary": "Hyperhumans is a group of exceptional individuals deploying code for the fourth industrial revolution. They are building an ecosystem of software that will help elevate and evolve human life in business and beyond.",
        "twitter": "https://twitter.com/hyperhumans",
        "url": "https://hyperhumans.ai",
        "youtube": null
      },
      {
        "children": [],
        "company_id": 2,
        "employees": [],
        "is_accepted": false,
        "name": "Bolt",
        "summary": "Bolt is the first European mobility super-app offering better alternatives for every purpose a private car serves, including ride-hailing, shared cars, scooters, and food and grocery delivery."
      }
    ]
  }
}
```

#### Accepting a Company

The following example accepts a company. This sets `is_accepted = True` in the `UserCompany` table. This method deducts credits from the user responds with the full company data. As the company has been accepted, all future responses by the user will the return its full company data.

```bash
curl \
--location https://api.neuralead.ai/company/<company_id>/accept \
--request POST \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json'
```

```json
{
  "data": {
    "company": {
      "children": [],
      "company_id": 2,
      "domain": "bolt.eu",
      "email": null,
      "employees": [],
      "facebook": "https://facebook.com/boltghana",
      "headcount": "1001-5000",
      "industry": "Transportation, Technology",
      "instagram": "https://instagram.com/bolt",
      "is_accepted": true,
      "keywords": "Mobility Super-App, Ride-Hailing, Shared Cars, Scooters, Food Delivery, Grocery Delivery",
      "linkedin": "https://linkedin.com/company/bolt-eu",
      "location": null,
      "name": "Bolt",
      "phone": null,
      "summary": "Bolt is the first European mobility super-app offering better alternatives for every purpose a private car serves, including ride-hailing, shared cars, scooters, and food and grocery delivery.",
      "twitter": "https://twitter.com/boltapp_gh",
      "url": "https://bolt.eu",
      "youtube": null
    }
  }
}
```

#### Finding Companies

The following route allows an `amount` of companies to be found without a parent company by only specifying the `industry` and `location`, which both default to `*` if not supplied.

```bash
curl \
--location https://api.neuralead.ai/company/find \
--request POST  \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
   "amount": 1,
   "industry": "Artificial Intelligence, Software Development",
   "location": "London"
}'
```

```json
{
  "data": {
    "companies": [
      {
        "children": [],
        "company_id": 3,
        "employees": [],
        "is_accepted": false,
        "name": "Unify.ai",
        "summary": "Unify.ai offers a platform that simplifies the landscape of Language Model (LLM) selection by providing a single API key to access all models from various providers. Their focus is on optimizing output quality, speed, and cost for developers."
      }
    ]
  }
}
```

## Employee

### Schema

#### Employee

| Key                  | Type    |              |
| :------------------- | :------ |:------------ |
| id                   | Integer | primary key  |
| name                 | String  | nullable     |
| email                | String  | nullable     |
| phone                | String  | nullable     |
| job_title            | String  | nullable     |
| job_title_best_match | String  | nullable     |
| linkedin             | String  | nullable     |
| company_id           | Integer | foreign key  |
| linkedin             | String  | nullable     |
| facebook             | String  | nullable     |
| twitter              | String  | nullable     |
| has_email            | Boolean |              |
| has_phone            | Boolean |              |
| has_linkedin         | Boolean |              |
| has_facebook         | Boolean |              |
| has_twitter          | Boolean |              |

#### UserEmployee

| Key       | Type    |              |
| :-------- | :------ |:------------ |
| user_employee_id | Integer | primary_key |
| user_id          | Integer | foreign key |
| employee_id      | Integer | foreign key | 
| is_accepted      | Boolean | default false |

### API Overview

### Curl Examples

| Method  | Endpoint                            | Description                                  |
| :-------| :---------------------------------- |:-------------------------------------------- |
| GET     | /employee/                          | Returns all employees.                       |
| GET     | /employee/<employee_id>             | Returns a specific employee.                 |
| POST    | /company/<company_id>/employee/find | Finds employees in specific company.         |

#### Find Employees Within a Company.

The following requests finds employees with a given `job_title` within a user-accepted company with a given `company_id`. The company must exist in the `Company` table and be accepted by the current user, i.e. `is_accepted = True` in the `UserCompany` table. All employees that are found are added to the `Employee` table and to the `UserEmployee` table. The returned employees are not accepted by default and therefore only a snippet of their data is returned:

```bash 
curl \
--location 'https://api.neuralead.ai/company/<company_id>/employee/find' \
--request POST \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "job_title": "Co-founder, Founder, CEO, Manager, Sales"
}'
```

```json
{
  "data": {
    "employees": [
      {
        "employee_id": 1,
        "has_email": true,
        "has_facebook": true,
        "has_linkedin": true,
        "has_phone": true,
        "has_twitter": false,
        "is_accepted": false,
        "job_title": "Co-Founder and CEO",
        "name": "Dinidh O'Brien"
      }
    ]
  }
}
```

**Note**. Now that employees have been found their snippet data will appear when getting data for the company that they belong to:

```bash
curl \
--location https://api.neuralead.ai/company/<company_id> \
--request GET \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

```json
{
  "data": {
    "company": {
      "children": [
        {
          "company_id": 2,
          "domain": "bolt.eu",
          "email": null,
          "facebook": "https://facebook.com/boltghana",
          "headcount": "1001-5000",
          "industry": "Transportation, Technology",
          "instagram": "https://instagram.com/bolt",
          "is_accepted": true,
          "keywords": "Mobility Super-App, Ride-Hailing, Shared Cars, Scooters, Food Delivery, Grocery Delivery",
          "linkedin": "https://linkedin.com/company/bolt-eu",
          "location": null,
          "name": "Bolt",
          "phone": null,
          "similarity": null,
          "summary": "Bolt is the first European mobility super-app offering better alternatives for every purpose a private car serves, including ride-hailing, shared cars, scooters, and food and grocery delivery.",
          "twitter": "https://twitter.com/boltapp_gh",
          "url": "https://bolt.eu",
          "youtube": null
        }
      ],
      "company_id": 1,
      "domain": "hyperhumans.ai",
      "email": "info@hyperhumans.ai",
      "employees": [
        {
          "employee_id": 1,
          "has_email": true,
          "has_facebook": true,
          "has_linkedin": true,
          "has_phone": true,
          "has_twitter": false,
          "is_accepted": false,
          "job_title": "Co-Founder and CEO",
          "name": "Dinidh O'Brien"
        }
      ],
      "facebook": null,
      "headcount": "1-10",
      "industry": "Artificial Intelligence, Software Development, Technology",
      "instagram": null,
      "is_accepted": true,
      "keywords": "A.I. interfaces, software ecosystem, 4th industrial revolution, beta testing program",
      "linkedin": "https://linkedin.com/company/gradivis-llc",
      "location": "Tallinn, Estonia",
      "name": "Hyperhumans",
      "phone": null,
      "summary": "Hyperhumans is a group of exceptional individuals deploying code for the fourth industrial revolution. They are building an ecosystem of software that will help elevate and evolve human life in business and beyond.",
      "twitter": "https://twitter.com/hyperhumans",
      "url": "https://hyperhumans.ai",
      "youtube": null
    }
  }
}
```

#### Accepting an Employee

The following endpoint accepts an employee with a given `employee_id`. The `UserEmployee` table is updated to have `is_accepted = True` and credits are deducted from the user's account. The full representation of the employee is returned.

```bash
curl \
--location 'https://api.neuralead.ai/employee/<employee_id>/accept' \
--request POST \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

```json
{
  "data": {
    "employee": {
      "email": "dob@hyperhumans.ai",
      "employee_id": 1,
      "facebook": "https://www.facebook.com/people/_/100006640031305",
      "is_accepted": true,
      "job_title": "Co-Founder and CEO",
      "job_title_best_match": "Co-Founder and CEO",
      "linkedin": "https://www.linkedin.com/in/dinidh",
      "name": "Dinidh O'Brien",
      "phone": "440-354-6805",
      "profile_pic_url": "https://b856yksr0bgjfswm.public.blob.vercel-storage.com/Hyperhumans_Dinidh%20O'Brien-x5f2UNnwOVRZyF35o8FuYPYfKuFjZ7",
      "twitter": null
    }
  }
}
```

**Note**. Now that the employee has been accepted it's full data is available.

#### Getting Employees

Employees can be fetched in a similar way to companies. The following gets all employees in that are present in the `UserEmployee` table. Similarly if the employee has been accepted then the full data is returned, otherwise only a snippet will be returned. Again, employees can be filtered by appending a query to the end of the URL, i.e. `?name=Dinidh`, or individually specifying the ID, i.e. `/<employee_id>`.

```bash
curl \
--location 'https://api.neuralead.ai/employee' \
--request GET \
--header 'Authorization: Bearer <YOUR_API_KEY>'
{
  "data": {
    "employees": [
      {
        "email": "dob@hyperhumans.ai",
        "employee_id": 1,
        "facebook": "https://www.facebook.com/people/_/100006640031305",
        "is_accepted": true,
        "job_title": "Co-Founder and CEO",
        "job_title_best_match": "Co-Founder and CEO",
        "linkedin": "https://www.linkedin.com/in/dinidh",
        "name": "Dinidh O'Brien",
        "phone": "440-354-6805",
        "profile_pic_url": "https://b856yksr0bgjfswm.public.blob.vercel-storage.com/Hyperhumans_Dinidh%20O'Brien-x5f2UNnwOVRZyF35o8FuYPYfKuFjZ7",
        "twitter": null
      }
    ]
  }
}
```

#### Getting Employees in Company

The following endpoint returns all employees in a given `company_id`.

```bash 
curl \
--location 'https://api.neuralead.ai/company/<company_id>/employee' \
--request GET \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

```json
{
  "data": {
    "employees": [
      {
        "email": "dob@hyperhumans.ai",
        "employee_id": 1,
        "facebook": "https://www.facebook.com/people/_/100006640031305",
        "is_accepted": true,
        "job_title": "Co-Founder and CEO",
        "job_title_best_match": "Co-Founder and CEO",
        "linkedin": "https://www.linkedin.com/in/dinidh",
        "name": "Dinidh O'Brien",
        "phone": "440-354-6805",
        "profile_pic_url": "https://b856yksr0bgjfswm.public.blob.vercel-storage.com/Hyperhumans_Dinidh%20O'Brien-x5f2UNnwOVRZyF35o8FuYPYfKuFjZ7",
        "twitter": null
      }
    ]
  }
}
```

#### Downloading Employee Profile Picture

The following endpoint returns the profile picture for a given employee with a given `employee_id` and pipes the data to file named `employee_profile_picture.png`.

```bash 
curl \
--location 'https://api.neuralead.ai/employee/<employee_id>/profile_picture' \
--request GET \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
> employee_profile_picture.png
```

### Example SQL

```sql
insert into company
(
    id,
    url,
    name,
    email,
    summary,
    industry,
    location,
    keywords,
    created_at,
    updated_at,
    domain,
    linkedin,
    headcount,
    twitter
)
values
(
    128,
    'https://hyperhumans.ai',
    'Hyperhumans',
    'info@hyperhumans.ai',
    'Hyperhumans is a group of exceptional individuals deploying code for the fourth industrial revolution. They are building an ecosystem of software that will help elevate and evolve human life in business and beyond.',
    'Software Development, Artificial Intelligence, Data Visualization, Virtual and Augmented Realities',
    'Tallinn, Estonia',
    'Artificial Intelligence, Data Visualization, Virtual Reality, Augmented Reality, Software Development',
    '2024-06-17T19:32:12.549951Z',
    '2024-09-17T14:09:13.010465Z',
    'hyperhumans.ai',
    'https://linkedin.com/company/gradivis-llc',
    '1-10',
    'https://twitter.com/hyperhumans'
);
```

```sql
insert into employee
(
  id,
  name,
  email,
  phone,
  job_title,
  job_title_best_match,
  linkedin,
  company_id,
  created_at,
  updated_at
)
values (
  1,
  'Dinidh O''Brien',
  'dob@hyperhumans.ai',
  '+372-533-20449',
  'Co-Founder & CEO',
  'CEO',
  'https://www.linkedin.com/in/dinidh',
  128,
  '2024-06-18T14:35:13.52507Z',
  '2024-06-20T13:33:33.270092Z'
);
```
