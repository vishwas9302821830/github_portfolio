from unittest.mock import patch
from urllib.error import HTTPError
from gitguard.analyzer import score_status, get_remote_url,get_recommendations,score,get_github_info


def test_score_status():
    assert score_status(95) == "Excellent"
    assert score_status(80) == "Good"
    assert score_status(60) == "Better"
    assert score_status(40) == "Try to improve"


@patch("gitguard.analyzer.run_git_command")
def test_get_remote_url_https(mock_run_git_command):
    mock_run_git_command.return_value = (
        "https://github.com/vishwas9302821830/github_portfolio.git"
    )

    owner, repo = get_remote_url()

    assert owner == "vishwas9302821830"
    assert repo == "github_portfolio"


@patch("gitguard.analyzer.run_git_command")
def test_get_remote_url_ssh(mock_run_git_command):
    mock_run_git_command.return_value = (
        "git@github.com:vishwas9302821830/github_portfolio.git"
    )

    owner, repo = get_remote_url()

    assert owner == "vishwas9302821830"
    assert repo == "github_portfolio"

@patch("gitguard.analyzer.get_branch_count")
@patch("gitguard.analyzer.get_commit_count")
@patch("gitguard.analyzer.get_working_tree_status")
def test_get_recommendations(mock_status, mock_commit_count, mock_branch_count):
    mock_status.return_value = "Dirty"
    mock_commit_count.return_value = 2
    mock_branch_count.return_value = 1

    recommendations = list(get_recommendations())

    assert "Commit your pending changes" in recommendations
    assert "Make more meaningful commits" in recommendations
    assert "Create/Use feature branches" in recommendations


@patch("gitguard.analyzer.get_recent_commits")
@patch("gitguard.analyzer.get_working_tree_status")
@patch("gitguard.analyzer.get_branch_count")
@patch("gitguard.analyzer.get_commit_count")
@patch("gitguard.analyzer.get_current_branch")
def test_score(
    mock_branch, mock_commit_count, mock_branch_count, mock_status, mock_recent_commits
):
    mock_branch.return_value = "master"
    mock_commit_count.return_value = 5
    mock_branch_count.return_value = 3
    mock_status.return_value = "Clean"
    mock_recent_commits.return_value = "abc123 Initial commit"

    health_score = score()

    assert health_score == 100


@patch("gitguard.analyzer.request.urlopen")
def test_get_github_info(mock_urlopen):
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = b"""
    {
        "stargazers_count": 10,
        "forks_count": 5,
        "open_issues_count": 2,
        "visibility": "public"
    }
    """

    info = get_github_info("vishwas9302821830", "github_portfolio")

    assert info["stars"] == 10
    assert info["forks"] == 5
    assert info["issues"] == 2
    assert info["visibility"] == "public"

@patch("gitguard.analyzer.request.urlopen")
def test_get_github_info_not_found(mock_urlopen, capsys):
    mock_urlopen.side_effect = HTTPError(
        url="https://api.github.com/repos/test/test",
        code=404,
        msg="Not Found",
        hdrs=None,
        fp=None,
    )

    info = get_github_info("test", "test")

    captured = capsys.readouterr()

    assert info is None
    assert "Repository not found" in captured.out
